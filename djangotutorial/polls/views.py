# I start this file by importing F, which is a class from django.db.models; F is used to refer to model field values directly in database queries
from django.db.models import F
# then I import HttpResponseRedirect from django.http, which is used to redirect the user to a different URL
from django.http import HttpResponseRedirect
# I import get_object_or_404 from django.shortcuts, which is a shortcut function that retrieves an object from the database or raises a 404 error if it doesn't exist; render is also imported from django.shortcuts, which is used to render a template with a context
from django.shortcuts import get_object_or_404, render
# I import reverse from django.urls, which is used to reverse-resolve URLs by their name
from django.urls import reverse
# I import generic from django.views, which is a module that provides generic class-based views for handling requests and responses
from django.views import generic
# I import the timezone module from django.utils, which provides utilities for working with time zones
from django.utils import timezone 
# I import the Choice and Question models from the current package (polls); these models represent the data structure of the poll application
from .models import Choice, Question
# the IndwexView class is a generic ListView that displays a list of questions; it inherits from generic.ListView
class IndexView(generic.ListView):
    # I set the template_name variable to "polls/index.html"; this is the template that will be used to render the list of questions
    template_name = "polls/index.html"
    # I set the context_object_name variable to "latest_question_list"; this is the name of the context variable that will be used in the template to refer to the list of questions                                      
    context_object_name = "latest_question_list"
    # the get_queryset method is overridden to return the last five published questions (not including those set to be published in the future)
    def get_queryset(self):
        """Return the last five published questions (not including those set to be published in the future).
        """
        # then I return the queryset of questions that are published (pub_date__lte=timezone.now()) and order them by publication date in descending order (order_by("-pub_date")); I limit the queryset to the last five questions using slicing [:5]
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            # :5 is used to limit the queryset to the last five questions
            :5
        ]
#  the DetailView class is a generic DetailView that displays the details of a specific question; it inherits from generic.DetailView
class DetailView(generic.DetailView):
    # I set the model variable to Question; this specifies the model that will be used to retrieve the object for the detail view
    model = Question
    # I set the template_name variable to "polls/detail.html"; this is the template that will be used to render the details of the question
    template_name = "polls/detail.html"
    # the get_queryset method is overridden to return the questions that are published (pub_date__lte=timezone.now()); this excludes any questions that aren't published yet
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        # I return the queryset of questions that are published (pub_date__lte=timezone.now()); Question.onjects.filter(pub_date__lte=timezone.now()) returns all questions that have a publication date less than or equal to the current time
        return Question.objects.filter(pub_date__lte=timezone.now())
# the ResultsView class is a generic DetailView that displays the results of a specific question; it inherits from generic.DetailView
class ResultsView(generic.DetailView):
    # I set the model variable to Question; this specifies the model that will be used to retrieve the object for the results view
    model = Question
    # I set the template_name variable to "polls/results.html"; this is the template that will be used to render the results of the question
    template_name = "polls/results.html"
# the vote function handles the voting process for a specific question; it takes the request and question_id as parameters
def vote(request, question_id):
    # I set the question variable to the question object retrieved from the database using get_object_or_404; this function returns a 404 error if the question doesn't exist
    question = get_object_or_404(Question, pk=question_id)
    # this try block attempts to get the selected choice from the request.POST data using the choice ID; if the choice ID is not found, it raises a KeyError
    try:
        # I set the selected_choice variable to the choice object retrieved from the database using the choice ID from the request.POST data; this retrieves the choice that corresponds to the selected choice ID
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    # this except block catches the KeyError exception; if the selected choice is not found, it raises a Choice.DoesNotExist exception 
    except (KeyError, Choice.DoesNotExist):
        # then I return an HTTP response with a 404 error if the choice doesn't exist
        return render(
            # request is the HTTP request object
            request,
            # "polls/detail.html" is the template that will be used to render the response
            "polls/detail.html",
            {
                # question is the question object that was retrieved from the database
                "question": question,
                # error_message is a custom error message that will be displayed in the template if the choice doesn't exist
                "error_message": "You didn't select a choice.",
            },
        )
    # this else block is executed if the selected choice is found; it increments the vote count for the selected choice by 1
    else:
        # selected_choice.votes is the number of votes for the selected choice; I use F("votes") to refer to the votes field directly in the database, and I increment it by 1
        selected_choice.votes = F("votes") + 1
        # I save the selected choice object to update the vote count in the database
        selected_choice.save()
        # then return an HTTP response redirecting to the results page of the question using reverse; this generates the URL for the results page based on the question ID
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))



