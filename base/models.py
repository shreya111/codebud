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
    # test_input = models.CharField(max_length=100)

    # test_output = models.CharField(max_length=100)

    def __str__(self):
        return (str(self.prob_id) + '.  ' + self.name)

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Submission(models.Model):
    class Verdict(models.TextChoices):
        Success = "SUCCESS"
        COMPILATION_ERROR = "COMPILATION_ERROR"
        Wrong_Output = "Wrong Output"
        Time_Limit_Exceeded = "TIME LIMIT EXCEEDED"
        Runtime_Error = "RUNTIME ERROR"

    submittedAt = models.DateTimeField(auto_now=True)

    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    verdict = models.CharField(
        max_length=20,
        choices=Verdict.choices
    )

    def __str__(self):
        return (str(self.problem))

    # def __str__(self):
    #     return self.problem.code + "_" + self.verdict

class TestCase(models.Model):
    input = models.CharField(max_length=500)
    output = models.CharField(max_length=500)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.problem) 
   







