from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone

# # Create your views here.
# def index(request):
#     # order the Question objects by pub_date descending and get the first 5 questions
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     developer_name = "Moahmed"
#     # loop through the latest_question_list and each question is initialized to q and get the question_text attribute then seperate questions by comma
    
#     # The context is a dictionary mapping template variable names to Python objects.
#     context = {
#         "latest_question_list": latest_question_list,
#         "developer_name": developer_name,
#         }
#     # output = ', '.join([q.question_text for q in latest_question_list])
    
#     # A shortcut: render()
#     return render(request, "polls/index.html", context)
#     # render: load template, fill context, return HttpResponse object
#     # It returns an HttpResponse object of the given template rendered with the given context.

# def detail(request, question_id):
#     # Raising a 404 error
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#         # the Http404 exception if a question with the requested ID doesn’t exist.
#     #     raise Http404("Question does not exist")
#     # return render(request, "polls/detail.html", {  "question": question})
#         # A shortcut: get_object_or_404()
#         question = get_object_or_404(Question, pk=question_id)
#         return render(request, "polls/detail.html", {"question": question})
        
  
  
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplat the question voting form
#         return render(
#             request,
#             "polls/detail.html",
#             {
#                 "question": question,
#                 "error_message" : "You didn't select a choice.",
#             },
#         )
#     else:
#         # F("votes") + 1 instructs the database to increase the vote count by 1.
#         selected_choice.votes = F("votes") + 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         # As the Python comment above points out, you should always return an HttpResponseRedirect after successfully dealing with POST data.
#         return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

  
# def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, "polls/results.html", {"question": question})



# Generic views
# Amend views(from hard code to generic views)
class HomeView(generic.TemplateView):
    template_name = "polls/home.html"


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        """Return the last five published qiestions(not including those set to be published in the future).
        """
        # List of Question objects
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
    
        # What Django does internally:
        # # Django creates this context automatically:
        # context = {
        #    "latest_question_list": Question.objects.order_by("-pub_date")[:5]
        # }

    
class DetailView(generic.DetailView):
    # model = Question → Django knows to do Question.objects.get(pk=url_param)
    # Model: Question → Context variable: question
    # Django automatically creates the question variable name using this rule based on the model name.:
    # Model: Question → Variable: question
    # model = Question  # ← This becomes "question" in template
    # Single Question object
    model = Question
    template_name = "polls/detail.html"
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message" : "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"