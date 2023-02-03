from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Choice
# Create your views here.
def index(request):
    ques_list=Question.objects.order_by('-pub_date')[:5]
    return render(request,'polls/index.html',{'que_list':ques_list})
def detail(request,question_id):
    return HttpResponse("You're looking at question {}".format(question_id))
def results(request,questoin_id):
    response="You're looking at the results of question {}".format(question_id)
    return HttpResponse(response)
def vote(request,question_id):
    return HttpResponse("You're votin on question {}.".format(question_id))
