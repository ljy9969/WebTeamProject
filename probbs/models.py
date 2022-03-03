from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta


# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=1, related_name='author_question')
    content = models.TextField()
    views = models.PositiveIntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    comments = models.PositiveIntegerField(null=True)
    question_like_count = models.ManyToManyField(User, related_name='like_question')

    class Meta:
        permissions = [
            ('can_create_doctor', 'Can Create a Doctor')
        ]

    def __str__(self):
        return self.title

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.create_date

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.create_date.date()
            return str(time.days) + '일 전'
        else:
            return False


class Comment(models.Model):
    post = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=1)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.content

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.create_date

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.create_date.date()
            return str(time.days) + '일 전'
        else:
            return False
