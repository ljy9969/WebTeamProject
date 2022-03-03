from django.contrib import admin
from diagnosis.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)