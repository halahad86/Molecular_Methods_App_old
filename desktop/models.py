from django.db import models
from django.contrib.auth.models import User

# Create your models here

#class User(models.Model):
 #   name = models.CharField(max_length=128)
  #  email = models.EmailField(primary_key=True)
   # password = models.CharField(max_length=128)
    #privilege = models.BooleanField(default=False)
    #lastScore = models.IntegerField(default=0)

    #def __unicode__(self):
     #   return self.name


class Result(models.Model):
    name = models.ForeignKey(User)
    question = models.ForeignKey('Question')
    answer = models.ForeignKey('Answer')

    def __unicode__(self):
        return self.name


class Question(models.Model):

    #Needed in order to have Static - hard coded question choices
    TOPICS_CHOICES = (
        (1, 'General'),
        (2, 'PCR & Primer'),
        (3, 'Restriction Mapping'),
        (4, 'Data Calculations'),
    )
    number = models.AutoField(primary_key=True)
    topic = models.IntegerField(choices=TOPICS_CHOICES, default=1)
    question = models.CharField(max_length=4096)
    #hint = models.CharField(max_length=4096)

    def __unicode__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey('Question')
    answer = models.CharField(max_length=128)
    correct = models.BooleanField(default=False)

    def __unicode__(self):
        return self.answer


class Video(models.Model):
    title = models.CharField(max_length=128, unique=True)
    link = models.URLField(max_length=256)
    topic = models.CharField(max_length=128)

    def __unicode__(self):
        return self.link


class Glossary(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=4096)

    def __unicode__(self):
        return self.title

class Lab(models.Model):
    name = models.CharField(max_length=256)
    #icon = models.FileField()
    number = models.IntegerField(unique=True)
    ILO = models.CharField(max_length=4096)
    tasks = models.CharField(max_length=32768)

    def __unicode__(self):
        return self.name
