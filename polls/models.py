from django.db import models
from django.utils import timezone  # 时区处理

import datetime


# Create your models here.

class Querstion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date published')

    # class Meta:  # 用于设置数据库中表的名字
    #     db_table: 'querstion'

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Querstion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=10)

    # class Meta:
    #     db_table: 'choice'

    def __str__(self):
        return self.choice_text
