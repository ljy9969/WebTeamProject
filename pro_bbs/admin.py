from django.contrib import admin
from pro_bbs.models import Question, Answer


# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
