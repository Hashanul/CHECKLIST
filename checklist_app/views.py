from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Chapter, ChecklistQuestion, OperatorResponse
from .serializers import (
    ChapterSerializer, ChecklistQuestionSerializer, OperatorResponseSerializer
)


# 1 List or Create Chapters
class ChapterListCreateView(generics.ListCreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    # permission_classes = [permissions.IsAuthenticated]


# 2 List or Create questions
class ChecklistQuestionListCreateView(generics.ListCreateAPIView):
    queryset = ChecklistQuestion.objects.all()
    serializer_class = ChecklistQuestionSerializer


# 3 question GET, Update & Delete refer by id.
class ChecklistQuestionListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChecklistQuestion.objects.all()
    serializer_class = ChecklistQuestionSerializer

