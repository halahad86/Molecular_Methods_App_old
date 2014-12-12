from django.db import models
from django.contrib.auth.models import User

# Create your models here

class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=128)
    privilege = models.BooleanField(default=False)
    lastScore = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Result(models.Model):
    name = models.ForeignKey("User")
    question = models.ForeignKey("Question")
    answer = models.ForeignKey("Answer")

    def __unicode__(self):
        return self.name


class Question(models.Model):
    topic = models.CharField(max_length=128)
    number = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=4096)
    hint = models.CharField(max_length=4096)

    def __unicode__(self):
        return self.number


class Answer(models.Model):
    question = models.ForeignKey("Question")
    answer = models.CharField(primary_key=True, max_length=128)
    correct = models.BooleanField(default=False)

    def __unicode__(self):
        return self.number


class Video(models.Model):
    title = models.CharField(max_length=128, unique=True)
    link = models.URLField(max_length=256, primary_key=True)
    topic = models.CharField(max_length=128)

    def __unicode__(self):
        return self.title


class Glossary(models.Model):
    title = models.CharField(max_length=128, primary_key=True)
    description = models.CharField(max_length=4096)

    def __unicode__(self):
        return self.title
