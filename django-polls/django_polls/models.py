from django.db import models
import  datetime
from django.utils import timezone
from django.contrib import admin

# Create your models here.
# we’ll create two models: Question and Choice. A Question has a question and a publication date. A Choice has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question.

# Question Model(2 fields question and publication date)
class Question(models.Model):
    # class variables = database field(column)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("data published") 
    # pub_date: machine readable name while data published: human readable name called verbose name(optional)
    # If you don’t supply one, Django auto-generates a readable name
    def __str__(self):
        return self.question_text
    
    # display() decorator
    @admin.display(
        boolean=True, 
        ordering="pub_date",
        description="Published recently?",
    )
    
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

# Choice Model(3 fields: question foreign key(Question Mddel) choice text, votes, and )
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # in the db table = question_id integer NOT NULL, stores the Question PK
    # ForeignKey = Choice FK field mapped to Question PK(auto genetare if you did not add the models field) field  
    # ForeignKey. That tells Django each Choice is related to a single Question. 
    # on_delete matters: #CASCADE deletes Choices if the Question is deleted.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text