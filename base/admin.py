from django.contrib import admin

# Register your models here.

from .models import Problem, Submission

admin.site.register(Problem)
admin.site.register(Submission)
