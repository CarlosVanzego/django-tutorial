# this file starts with me importing the datetime module, which is used to work with dates and times in Python
import datetime
# then I import the models module from the django.db module, which provides the base classes for cretaing database models
from django.db import models
# I also import the timezone module from django.utils, which provides utilities for working with time zones
from django.utils import timezone
# lastly, I import the admin module from django.contrib, which is used to create an admin interface for the models
from django.contrib import admin
# the Question class represents questions in the poll application; models.Model is the base class for all models in Django
class Question(models.Model):
    # question_text is a CharField, which is a field for storing character data; max_length specifies the maximum length of the field (here it is 200 characters)
    question_text = models.CharField(max_length=200)
    # pub_date is a DateTimeField, which is a field for storing date and time data; it represents the date and time when the question was published
    pub_date = models.DateTimeField("date published")
    # the __str__ method returns a string representation of the object; in this case, it returns the question_text
    def __str__(self):
        # here I am returning the question_text attribute of the Question object
        return self.question_text
    # the was_published_recently method checks if the question was published within the last day; it returns True if the question was published recently, and False otherwise
    def was_published_recently(self):
        # I set the now variable to the current date and time using timezone.now()
        now = timezone.now()
        # then I check if the pubn_date is within the last day; if it is, I return True,. otherwise I return False
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    # @amin.display is a decorator that adds metadata to the method; it specifies how the method should be displayed in the Django admin interface
    @admin.display(
        # boolean=True means that ther method will be displayed as a boolean value (True or False) in the admin interface 
        boolean=True,
        # ordering=pub_date means that the method will be ordered by the pub_date field in the admin interface
        ordering=pub_date,
        # description="Published recently?" provides a human-readable description of the method in the admin iunterface
        description="Published recently?",
    )
    # the was_published_recently method checks if the question was published within the last day; it returns True if the question was published recerntly, and False otherwise
    def was_published_recently(self):
        # I set the now variable to the current date and time using timezone.now()
        now = timezone.now()
        # then I chek if the pub_date is within the last day; if it is, I return True, otherwise I return False
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
# the Choice class represents choices for a question in the poll application; it also inherits from models.Model
class Choice(models.Model):
    # the question variable is a foreign key that creates a many-to-one relationship between the Choice and Question models; it means that each choice is related to one question, but a question can have multiple choices 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # choice_text is a CharField, which is a field for storing character data; max_length specifies the maximum length of the field (here it is 200 characters)
    choice_text = models.CharField(max_length=200)
    # votes is an IntegerField, which is a field for storing integer data; it represents the number of votes for the choice
    votes = models.IntegerField(default=0) 
    # the __str__ method returns a string representation of the object; in this case, it returns the choice_text
    def __str__(self):
        # here, I am returning the choice_text attribute of the Choice object
        return self.choice_text   
    