from multiprocessing import context
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.http import HttpResponse
from .models import Problem


# Create your views here.

def home(request):
    problems= Problem.objects.all()
    context={
        'problems' : problems
    }
    return render(request, 'base/home.html', context)

def problem_detail(request, pk):
    detail=Problem.objects.get(prob_id=pk)
    context={
        'detail': detail
    }
    return render(request, 'base/problem_detail.html', context)




