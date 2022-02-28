from django.db import models


# Create your models here.

class Question(models.Model):
    Q_subject = models.CharField(max_length=50)
    Q_content = models.TextField()
    Q_author = models.CharField(max_length=20)
    Q_current_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Q_subject


class Answer(models.Model):
    A_content = models.TextField()
    A_author = models.CharField(max_length=20)
    A_current_date = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.A_content
