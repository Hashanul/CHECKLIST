from django.urls import path
from . import views

urlpatterns = [
    path('chapters/', views.ChapterListCreateView.as_view(), name='chapter_list'),
    path('questions/', views.ChecklistQuestionListCreateView.as_view(), name='question_list'),
    path('questions/<int:pk>/', views.ChecklistQuestionListDetailView.as_view(), name='question_detail'),

]
