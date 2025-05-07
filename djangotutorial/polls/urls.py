# I start this file by importing the path function from django.urls, which is used to define URL patterns in Django
from django.urls import path

# then I'm importing views from the current packcage (polls); views is a module that contains the view functions and classes for handling requests and responses in the poll application
from . import views
# I set the app_name variable to "polls"; this is used to namespace the URL patterns in the application
app_name = "polls"
# urlpatterns is a list of URL patterns for the poll application; each pattern is defined using the path function
urlpatterns = [
    # "" is the root URL pattern; views.IndexView,as_view() is a class-based view that handles requests to the index page of the poll application; name="index" gives this URL pattern a name, which can be used to refer to it in templates and views   
    path("", views.IndexView.as_view(), name="index"),
    # "<int:pk>?" is a URL pattern that captures an integer value (pk) from the URL; views.DetailView.as_view() is a class-based view that handles requests to the detail page of a specific question; name="detail" gives this URL pattern a name
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # "<int:pk>/results/" is a URL pattern that captures an integer value (pk) from the URL; views.ResultsView.as_view() is a class-based view that handles requests to the results page of a specific question; name="results" gives this URL pattern a name
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # "<int:question_id>/vote/" is a URL pattern that captures an integer value (question_id) from the URL; views.vote is a function-based view that handles requests to vote on a specific question; name="vote" gives this URL pattern a name
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
