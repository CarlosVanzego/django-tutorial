# I start this file by importing the datetime module, which is used to work with dates and times in Python
import datetime 
# then I import the TestCase class from django.test, which is used to create test cases for Django applications
from django.test import TestCase
# I also import the timezone module from django.utils, which provides utilities for working with time zones
from django.utils import timezone
# I import the reverse function from django.urls, which is used to reverse URL patterns in Django
from django.urls import reverse
# I import the Question model from the current package (polls); this is the model that represents questions in the poll application
from .models import Question
# the QuestionModelTests class is a test case for the Question model; it inherits from TestCase, which provides methods for creating and running tests
class QuestionModelTests(TestCase):
    # this method tests the was_published_recently() method of the Question model
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns false for questions whose pub_date is in the future.
        """
        # I set the time variable to a date and time 30 days in the future using timezone.now() and datetime.timedelta
        time = timezone.now() + datetime.timedelta(days=30)
        # I created a future_question object with a pub_date in the future
        future_question = Question(pub_date=time)
        # self.assertIs() is used to check if the was_published_recently() method returns False for the future_question object
        self.assertIs(future_question.was_published_recently(), False)
    # this method tests the was_published_recently() method of the Question model
    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns false for questions whose pub_date is older than 1 day
        """
        # I set the time variable to a date and time 1 day and 1 second in the past using timezone.now() and datetime.timedelta
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        # I created an old_question object with a pub_date in the past
        old_question = Question(pub_date=time)
        # self.assertIs() is used to check if the was_published_recently() method returns False for the old_question object
        self.assertIs(old_question.was_published_recently(), False)
    # this method tests the was_published_recently() method of the Question model
    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date is within the last day 
        """ 
        # I set the time variable to a date and time 23 hours, 59 minutes, and 59 seconds in the past using timezone.now() and datetime.timedelta
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        # I created a recent_question object with a pub_date in the past
        recent_question = Question(pub_date=time)
        # self.assertIs() is used to check if the was_published_recently() method returns True for the recent_question object
        self.ssertIs(recent_question.was_published_recently(), True)   
    # this method creates a question with the given question_text and published the given number of days offset to now
    def create_question(question_text, days):
        """
        Create a question with the given `question_text` and published the
        given number of `days` offset to now (negative for questions published
         in the past, positive for questions that have yet to be published).
         """
        # I set the time variable to a date and time offset by the given number of days using timezone.now() and datetime.timedelta
        time = timezone.now() + datetime.timedelta(days=days)
        # then I am returning a new Question object created with the given question_text and pub_date; question_text is the text of the question, and pub_date is the date and time when the question was published
        return Question.objects.create(question_text=question_text, pub_date=time)

# the QuestionIndexViewTests class is a test case for the index view of the poll application; it inherits from TestCase, which provides methods for creating and running tests
class QuestionIndexViewTests(TestCase):
    # the test_no_questions method tests the index view when no questions exist
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        # I set response to the result of calling the index view using self.client.get() and the reverse function to get the URL for the index view
        response = self.client.get(reverse("polls:index"))
        # self.assertEqual() is used to check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # self.assertContains() is used to check if the response contains the message "No polls are available."
        self.assertContains(response, "No polls are available.")
        # self.assertQuerySetEqual() is used to check if the latest_question_list context variable is empty
        self.assertQuerySetEqual(response.context["latest_question_list"], [])
    # this method tests the index view when a question with a pub_date in the past exists
    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        # I created a past question with a pub_date in the past using the create_question method
        question = create_question(question_text="Past question.", days=-30)
        # I set response to the result of calling the index view using self.client.get() and the reverse function to get the URL for the index view
        response = self.client.get(reverse("polls:index"))
        # self.assertQuerySetEqual() is used to check if the response contains the question in the latest_question_list context variable
        self.assertQuerySetEqual(
            # response.context["latest_question_list"] is the context variable that contains the list of questions to be displayed on the index page
            response.context["latest_question_list"],
            # [question] is a list containing the question object that was created earlier
            [question],
        )
    # this method tests the index view when a question with a pub_date in the future exists
    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on the index page.
        """ 
        # I created a future question with a pub_date in the future using the create_question method
        create_question(question_text="Future question.", days=30)
        # I set response to the result of calling the index view using self.client.get() and the reverse function to get the URL for the index view
        response = self.client.get(reverse("polls:index"))
        # self.assertContains() is used to check if the response status code is 200 (OK)
        self.assertContains(response, "No polls are available.")
        # self.assertQuerySetEqual() is used to check if the latest_question_list context variable is empty
        self.assertQuerySetEqual(response.context["latest_question_list"], [])
    # this method tests the index view when both past and future questions exist
    def test_future_quesiton_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions are displayed.
        """    
        # I created a past question with a pub_date in the past using the create_question method
        question = create_question(question_text="Past question.", days=-30)
        # I created a future question with a pub_date in the future using the create_question method
        create_question(question_text="Future question.", days=30)
        # I set response to the result of calling the index view using self.client.get() and the reverse function to get the URL for the index view
        response = self.client.get(reverse("polls:index"))
        # self.assertQuerySetEqual() is used to check if the response contains the question in the latest_question_list context variable
        self.assertQuerySetEqual(
            # response.context["latest_question_list"] is the context variable that contains the list of questions to be displayed on the index page
            response.context["latest_question_list"],
            # [question] is a list containing the question object that was created earlier
            [question],
        )   
    # this method tests the index view when multiple past questions exist
    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.        
        """    
        # I created two past questions with pub_dates in the past using the create_question method
        question1 = create_question(question_text="Past question 1.", days=-30)
        # this is the second past question
        question2 = create_question(question_text="Past question 2.", days=-5)\
        # I set response to the result of calling the index view using self.client.get() and the reverse function to get the URL for the index view
        response = self.client.get(reverse("polls:index"))
        # self.assertQuerySetEqual() is used to check if the response contains the questions in the latest_question_list context variable
        self.assertQuerySetEqual(
            # response.context["latest_question_list"] is the context variable that contains the list of questions to be displayed on the index page
            response.context["latest_question_list"],
            # [question2, question1] is a list containing the two question objects that were created earlier
            [question2, question1],
        )          
# this class is a test case for the detail view of the poll application; it inherits from TestCase, which provides methods for creating and running tests
class QuestionDetailViewTests(TestCase):
    # this method creates a question with the given question_text and published the given number of days offset to now
    def test_future_question(self):
        """
        the detail view of a question with a pub_date in the future returns a 404 not found. 
        """
        # I created a future question with a pub_date in the future using the create_question method
        future_question = create_question(question_text="Future question.", days=5)
        # I set the url variable to the result of calling the reverse function to get the URL for the detail view of the future question
        url = reverse("polls:detail", args=(future_question.id,))
        # I set response to the result of calling the detail view using self.client.get() and the url variable
        response = self.client.get(url)
        # self.assertEqual() is used to check if the response status code is 404 (not found)
        self.assertEqual(response.status_code, 404)
    # this method tests the detail view when a question with a pub_date in the past exists
    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past displays the question's text.
        """   
        # I created a past question with a pub_date in the past using the create_question method
        past_question = create_question(question_text="Past Question.", days=-5)
        # I set the url variable to the result of calling the reverse function to get the URL for the detail view of the past question
        url = reverse("polls:detail", args=(past_question.id,))
        # I set response to the result of calling the detail view using self.client.get() and the url variable
        response = self.client.get(url)
        # self.assertContains() is used to check if the response contains the question text; response is the HTTP response object returned by the detail view, and past_question.question_text is the text of the question
        self.assertContains(response, past_question.question_text)

        