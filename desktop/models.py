from django.db import models
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from Mapping import findAns

# Custom User model. Currently using default Django user model

#class User(models.Model):
#   name = models.CharField(max_length=128)
#  email = models.EmailField(primary_key=True)
# password = models.CharField(max_length=128)
#privilege = models.BooleanField(default=False)
#lastScore = models.IntegerField(default=0)

#def __unicode__(self):
#   return self.name

# This is for a Restriction Mapping question


class MQuestion(models.Model):
    Number = models.IntegerField(primary_key=True)
    Size = models.IntegerField(help_text ="All numbers give should be round numbers e.g 35 instead of 3.5 or 60 instead of 6.0")
    Enzyme1 = models.CharField(max_length=200,help_text ="Please enter Enzymes such that they are of the form Name:size of the slice:size of the slice  e.g Exoir:20:50")
    Enzyme2 = models.CharField(max_length=200, help_text ="Note the colons between section in the Enzyme e.g Xoire:70")
    Enzyme3 = models.CharField(max_length=200)
    Answer = models.CharField(max_length=200, editable = False)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.Enzyme1

    def save(self, *args, **kwargs):
        ans = findAns(self.Size,self.Enzyme1,self.Enzyme2,self.Enzyme3)
        if ans == "NoSol":
            print ""
        else:
            self.Answer = ans
            super(MQuestion, self).save(*args, **kwargs) # Call the "real" save() method.

    class Meta:
        verbose_name="a new restriction mapping question"
        verbose_name_plural = "Restriction mapping questions"

# May not need this model is we are not storing the user's result
class Result(models.Model):
    name = models.ForeignKey(User)
    question = models.ForeignKey('QQuestion')
    answer = models.ForeignKey('Answer')

    def __unicode__(self):
        return self.name

# This is for a Quiz question


class QQuestion(models.Model):

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

    class Meta:
        verbose_name="a new quiz question"
        verbose_name_plural = "Quiz questions"


class Answer(models.Model):
    question = models.ForeignKey('QQuestion')
    answer = models.CharField(max_length=128)
    correct = models.BooleanField(default=False)

    def __unicode__(self):
        return self.answer

    class Meta:
        verbose_name="a new quiz answer"
        verbose_name_plural = "Quiz answers"


class Video(models.Model):
    title = models.CharField(max_length=128, unique=True)
    link = models.URLField(max_length=256)
    topic = models.CharField(max_length=128)

    def __unicode__(self):
        return self.link

    class Meta:
        verbose_name="a new video"
        verbose_name_plural = "Videos"


class Glossary(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=4096)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name="a new Glossary term"
        verbose_name_plural = "Glossary"


class Lab(models.Model):
    name = models.CharField(max_length=256)
    #icon = models.FileField()
    number = models.IntegerField(unique=True)
    ILO = models.CharField(max_length=4096)
    tasks = models.CharField(max_length=32768)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name="a new lab session"
        verbose_name_plural = "Labs"

