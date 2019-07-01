from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/add/', views.QuestionCreate.as_view(), name='question-add'),
    path('questions/', views.QuestionListView.as_view(), name='questions'),
    path('answers/', views.AnswerListView.as_view(), name='answers'),
    path('question/<int:pk>', views.QuestionDetailView.as_view(), name='question-detail'),
    path('question/<int:pk>/upvote/', views.QuestionDetailView.as_view(), name='answer-upvote'),
    path('question/<int:pk>/answer/', views.AnswerCreate.as_view(), name='answer-add'),
    # path('question/<int:pk>/downvote/', views.QuestionDetailView.as_view(), name='question-detail'),

    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('author/add/', views.AuthorCreate.as_view(), name='author-add'),
    path('author/<int:pk>/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),

]