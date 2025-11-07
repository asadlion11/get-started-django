from django.urls import path
from . import views

# hard code view
# app_name = "polls"
# urlpatterns = [
    #ex: /polls/
    # path('', views.index, name='index'),
    
    # ex: /polls/5/
    # eg: if the urls is: /polls/5
    # Django calls the view: views.detail(request, question_id=5). this is beahind scene,
    # behind the scenes Django resolves the URL pattern and calls the view function like: views.detail(request, question_id=5)
    # That question_id=5 is not magic — it comes from the URL pattern that matched the request.
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote', views.vote, name='vote'),
# ]

# Generic views
# Amend URLconf
app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:question_id>/vote", views.vote, name="vote"),
    path("<int:pk>/results", views.ResultsView.as_view(), name="results")
]
