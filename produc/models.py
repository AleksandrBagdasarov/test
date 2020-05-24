from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class products(models.Model):
    title       = models.CharField(max_length=120,)
    discription = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    summary     = models.TextField(blank=False, null=False)
    futured     = models.BooleanField()

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def  was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text