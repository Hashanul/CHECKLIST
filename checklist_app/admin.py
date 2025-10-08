from django.contrib import admin
from .models import Chapter, ChecklistQuestion, OperatorResponse, DocumentReference


admin.site.register(Chapter)
admin.site.register(ChecklistQuestion)
admin.site.register(OperatorResponse)
admin.site.register(DocumentReference)