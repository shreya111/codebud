from multiprocessing import context
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.http import HttpResponse
from .models import Problem
from .models import Topic, User
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    problems= Problem.objects.all()
    context={
        'problems' : problems
    }
    return render(request, 'base/home.html', context)

@login_required(login_url='login')
def problem_detail(request, pk):
    detail=Problem.objects.get(prob_id=pk)
    context={
        'detail': detail
    }
    return render(request, 'base/problem_detail.html', context)

def submit_Problem(request, py):
    submitcode=Problem.objects.get(prob_id=py)
    context={
        'submitcode':submitcode
    }
    return render(request, 'base/submit_Problem.html', context)

def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'base/topic.html', {'topics': topics})

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'base/profile.html', context)




