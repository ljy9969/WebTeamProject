from django.db import models


# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateTimeField()
    # null=True => db에서 modify_data 칼럼에 null을 허용
    # blank=True => form.is_vaild() 입력데이터 검사 시 값이 없어도 가능
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)