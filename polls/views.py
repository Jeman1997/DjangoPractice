from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Hello World!')
def detail(request,question_id):
    return HttpResponse("You're looking at question {}".format(question_id))
def results(request,questoin_id):
    response="You're looking at the results of question {}".format(question_id)
    return HttpResponse(response)
def vote(request,question_id):
    return HttpResponse("You're votin on question {}.".format(question_id))
