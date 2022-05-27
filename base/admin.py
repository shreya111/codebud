from django.contrib import admin

# Register your models here.

from .models import Problem, Submission, Topic, TestCase

admin.site.register(Problem)
admin.site.register(Submission)
admin.site.register(Topic)
admin.site.register(TestCase)
