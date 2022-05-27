from multiprocessing import context
from urllib import request
from datetime import datetime
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.test import TestCase
from .models import Problem, Submission
from .models import Topic, User, Problem, TestCase
from django.contrib.auth.decorators import login_required
import subprocess
from django.urls import reverse

COMPILE = ["g++", "temp.cpp"]
RUN = ["./a.out"]

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


def submit(request, question_id):
    code = request.POST['code']
    with open('temp.cpp', 'w') as file:
        file.write(code)

    _compile = subprocess.run(COMPILE, shell=True)
    if (_compile.returncode != 0):
        verdict = Submission.Verdict.COMPILATION_ERROR
    else:
        tests = TestCase.objects.filter(problem_id = question_id)
        verdict = Submission.Verdict.Success
        for test in tests:
            input = test.input
            expected = test.output
            try:
                _run = subprocess.run(RUN, stdout=subprocess.PIPE,input=str(input), encoding='ascii', timeout=1, shell=True)
                print(_run.stdout)
                print(_run.stderr)
                actual = _run.stdout
                if (expected != actual):
                    verdict = Submission.Verdict.Wrong_Output
                    break
                else:
                    verdict = Submission.Verdict.Success
            except subprocess.TimeoutExpired:
                verdict = Submission.Verdict.Time_Limit_Exceeded
                break
            except Exception as e:
                verdict = Submission.Verdict.Runtime_Error
                print(e)
                break

    sol = Submission(
        problem = Problem.objects.get(pk = question_id),
        verdict = verdict,
        submittedAt = datetime.now
    )
    sol.save()

    return HttpResponseRedirect(reverse('leaderboard'))

def leaderboard(request):
    recent_submissions = Submission.objects.all().order_by('-submittedAt')[:10]
    return render(request, 'base/leaderboard.html', {"result": recent_submissions})

def problem_verdict(request, question_id):
    code_verdict=Problem.objects.get(prob_id=question_id)
    context = {
        'code_verdict' : code_verdict
    }
    return render(request, 'base/verdict.html', context)

    



