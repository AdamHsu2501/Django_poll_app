from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    
    RADIO = 'radio'
    CHECKBOX = 'checkbox'
    INPUT_TYEP = [
        (RADIO, RADIO),
        (CHECKBOX, CHECKBOX),
    ]
    
    type = models.CharField(
        null=False,
        max_length=20,
        choices=INPUT_TYEP,
        default=RADIO
    )
    
    def __str__(self):
        return self.title
    

class Option(models.Model):
    title = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    options = models.ManyToManyField(Option)
    
    def __str__(self):
        options = []
        for option in self.options.all():
            options.append(option.title)
        return '{}: {} {}'.format(self.user.username, self.question.title, ','.join(options))
    