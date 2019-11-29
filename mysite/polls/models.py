from django.db import models
from .enums import QuestionTypeEnum

# Your model here
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')
    type = models.CharField(max_length=30, choices=[(i.value, i.name) for i in QuestionTypeEnum],
                            null=False, blank=False, default=QuestionTypeEnum.EASY.value)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
