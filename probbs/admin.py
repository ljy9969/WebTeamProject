from django.contrib import admin
from probbs.models import Question, Comment


# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'views',
        'create_date',
    )
    search_fields = ('title', 'content', 'author__user_id')


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'content',
        'author',
        'create_date',
        'deleted',
    )
    search_fields = ('post__title', 'content', 'author__user_id',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Comment, CommentAdmin)

