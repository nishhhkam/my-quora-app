from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances
from django.contrib import admin
from django.contrib.auth.models import User
from datetime import date

class Comment(models.Model):

    """Model representing a question."""
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    answer = models.ForeignKey('Answer', on_delete=models.SET_NULL, null=True)
    comment_text = models.TextField(max_length=1000, help_text='Enter your comment...')
    date_created = models.DateField(null=True, blank=True)
    date_updated = models.DateField(null=True, blank=True)

    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.comment_text[:20]}..'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'author', 'date_created')
    list_filter = ('date_created', 'author')


class Answer(models.Model):

    """Model representing a question."""
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True)
    answer_text = models.TextField(max_length=2000, help_text='Write your answer here...')
    date_created = models.DateField(null=True, blank=True)
    date_updated = models.DateField(null=True, blank=True)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        """String for representing the Model object."""
        return f'Que: {self.question.question_text[:50]}.. Ans: {self.answer_text[:50]}..'


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer_text', 'author', 'date_created', 'upvote', 'downvote', 'views')
    list_filter = ('date_created', 'author', 'upvote', 'downvote', 'views')
    fieldsets = (
        (None, {
            'fields': ('author','question', 'answer_text')
        }),
        ('Dates', {
            'fields': ('date_created', 'date_updated')
        }),
        ('Actions', {
            'fields': ('upvote', 'downvote','views')
        }),
    )

class Question(models.Model):

    """Model representing a question."""
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    question_text = models.TextField(max_length=1000, help_text='Enter your question in brief∂')
    date_created = models.DateField(null=True, blank=True)
    date_updated = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        """Returns the url to access a particular question and its answer."""
        return reverse('answers')

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.question_text}'


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'author', 'date_created')
    list_filter = ('date_created', 'author')


class Author(models.Model):

    """Model representing an author."""
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=70,blank=True)
    date_created = models.DateField(null=True, blank=True)
    credits = models.IntegerField(default=0)


    # def get_absolute_url(self):
    #     """Returns the url to access a particular author instance."""
    #     return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.username}'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_created', 'credits')
    