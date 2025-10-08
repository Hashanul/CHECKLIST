from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chapter(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} - {self.subject}"
    
class ChecklistQuestion(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='questions')
    question_no = models.PositiveIntegerField()
    question_text = models.TextField()
    reference_code = models.CharField(max_length=50, help_text="Reference to ANO-14-I (3.1.1)")

    def __str__(self):
        return f"Q {self.question_no}: {self.question_text}"
    
class OperatorResponse():
    """Response by operator against each question"""
    RESPONSE_CHOICES = [
        ('YES', 'Yes'),
        ('NO', 'No'),
        ('NA', 'Not Applicable'),
    ]
    STATUS_CHOICES = [
        ('S', 'Satisfactory'),
        ('NS', 'Not Satisfactory'),
    ]


    question = models.ForeignKey(ChecklistQuestion, on_delete=models.CASCADE, related_name="responses")
    operator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    response = models.CharField(max_length=4, choices=RESPONSE_CHOICES)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True, help_text="Include documentation reference or reason for non-compliance")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.question.question_no} - {self.response}"

class DocumentReference(models.Model):
    """Optional: store document links used in remarks"""
    response = models.ForeignKey(OperatorResponse, on_delete=models.CASCADE, related_name='documents')
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='references/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    