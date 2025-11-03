from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    # order the Question objects by pub_date descending and get the first 5 questions
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    developer_name = "Moahmed"
    # loop through the latest_question_list and each question is initialized to q and get the question_text attribute then seperate questions by comma
    
    # The context is a dictionary mapping template variable names to Python objects.
    context = {
        "latest_question_list": latest_question_list,
        "developer_name": developer_name,
        }
    # output = ', '.join([q.question_text for q in latest_question_list])
    return render(request, "polls/index.html", context)
    # render: load template, fill context, return HttpResponse object
    # It returns an HttpResponse object of the given template rendered with the given context.

def detail(request, question_id):
    return HttpResponse(f"You are looking the detail of the question {question_id}")

def results(request, question_id):
    return HttpResponse(f"You are looking the result of the question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You are voting the question {question_id}")