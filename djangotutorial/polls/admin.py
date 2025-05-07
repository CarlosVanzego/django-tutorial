# I am importing the admin moddle from django.contrib
from django.contrib import admin
# then I am importing the Choice class and Quesiton class from the .models module
from .models import Choice, Question
# this is a class called ChoiceInLine that inherits from the TabularInLine class
class ChoiceInline(admin.TabularInline):
    # I set the model variable to the Choice class
    model = Choice
    # I set the extra variable to 3, which means that 3 empty choice fields will be displayed
    extra = 3
# I created the QuestionAdmin class that inherits from the ModelAdmin class
class QuestionAdmin(admin.ModelAdmin):
    # fieldsets is a list of tuples that defines the layout of the admin form
    # the first element of each tuple is the title of the fieldset
    # the second element is a dictionary that defines the fields in the fieldset
    fieldsets = [
        # None is a special value that means that the fieldset will not have a title
        # the fields key is a list of fields that will be displayed in the fieldset
        # question_text is the field that will be displayed in the fieldset
        (None, {"fields": ["question_text"]}),
        # Date informationis the title of the fieldset
        # fileds is a dictionary that defines the fields in the fieldset
        # pub_date is the filed that will be displayed in the fieldset
        # classes is a list of CSS classes that will be applied to the fieldset
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    # inLines is a list of inLine classes that will be displayed in the admin form
    inlines = [ChoiceInline]
    # list_display is a list of fields that will be displayed in the admin list view; question_text is the field that will be displayed in the list view; pub_date is the field that will be displayed in the list view; was_published_recently is a method that will be displayed in the list view
    list_display = ["question_text", "pub_date", "was_published_recently"]
    # last_filter is a list of fields that will be used to filter the admin list view; pub_date is the field that will be used to filter the list view
    list_filter = ["pub_date"]
    # search_fields is a list of fields that will be used to search the admin list view; question_text is the field that will be used to search the list view
    search_fields = ["question_text"]
# admin.site.register is a function that registers the Question class with the admin site
# Question is the model that will be displayed in the admin list view
# QuestionAdmin is the class that will be used to display the Question model in the admin list view
admin.site.register(Question, QuestionAdmin)

