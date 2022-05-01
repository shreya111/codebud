from pickle import TRUE
from turtle import update
from unicodedata import name
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User


# Create your models here.



class Problem(models.Model):

    prob_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    description = models.TextField(null=True, blank=True)
    
    difficulty = models.CharField(max_length=20)

    updated = models.DateTimeField(auto_now=True)

    created = models.DateTimeField(auto_now_add=True)
    #timelimit
    #memorylimit
    testcases = models.CharField(max_length=100)

    def __str__(self):
        return (str(self.prob_id) + '.  ' + self.name)

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Submission(models.Model):
    submittedAt = models.DateTimeField(auto_now=True)

    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)





