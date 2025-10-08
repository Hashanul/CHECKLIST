from rest_framework import serializers
from .models import Chapter, ChecklistQuestion, OperatorResponse, DocumentReference


class DocumentReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentReference
        fields = ['id', 'name', 'file']


class OperatorResponseSerializer(serializers.ModelSerializer):
    operator = serializers.ReadOnlyField(source='operator.username')
    documents = DocumentReferenceSerializer(many=True, read_only=True)

    class Meta:
        model = OperatorResponse
        fields = [
            'id', 'question', 'operator', 'response', 'status',
            'remarks', 'documents', 'created_at'
        ]


class ChecklistQuestionSerializer(serializers.ModelSerializer):
    chapter = serializers.StringRelatedField()
    responses = OperatorResponseSerializer(many=True, read_only=True)

    class Meta:
        model = ChecklistQuestion
        fields = ['id', 'chapter', 'question_no', 'question_text', 'reference_code', 'responses']


class ChapterSerializer(serializers.ModelSerializer):
    questions = ChecklistQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Chapter
        fields = ['id', 'title', 'subject', 'questions']
