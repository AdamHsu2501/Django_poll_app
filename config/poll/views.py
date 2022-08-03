from collections import defaultdict
from msilib.schema import CheckBox
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Question, Option, Submission
# Create your views here.

class UserLoginView(LoginView):
    template_name = 'poll/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse('question-list')
    
class UserRegisterView(FormView):
    template_name = 'poll/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('question-list')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegisterView, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('question-list')
        return super(UserRegisterView, self).get(*args, **kwargs)
    
    
class QusetionListView(ListView):
    model = Question
    template_name = 'poll/question_list.html'
    
    

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'poll/question.html'
    context_object_name = 'question'
       

def submit(request, question_id):
    print('submit................................')

    if request.method == 'POST':
        curruser = request.user
        question = Question.objects.get(pk=question_id)
        print('curruser, question', curruser, question)
        try:
            submission = Submission.objects.get(user=curruser, question=question)
            submission.options.set([])
        except:
            submission = Submission.objects.create(user=curruser, question=question)
        print('submission...........', submission)
        answers = extract_answers(request)
        
        for answer in answers:
            submission.options.add(Option.objects.get(id=answer))
            
        submission.save()
        return HttpResponseRedirect(reverse(viewname='result', args=(question_id,)))
    else:
        return HttpResponseRedirect(reverse(viewname='question', args=(question_id,)))

def extract_answers(request):
   submitted_anwsers = []
   for key in request.POST:
       if key.startswith('option'):
           value = request.POST[key]
           option_id = int(value)
           submitted_anwsers.append(option_id)
   return submitted_anwsers

class QuestionResultView(DetailView):
    model = Question
    template_name = 'poll/question_result.html'
    context_object_name = 'question'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = context['question']
        
        try:
            user_submission = Submission.objects.get(question=question, user=self.request.user)
            user_options = [option.pk for option in user_submission.options.all()]
        except:
            user_options = []

        
        submisstions = question.submission_set.all()
        
        count_options = defaultdict(int)
        for submission in submisstions:
            for option in submission.options.all():
                count_options[option.pk] += 1
        submission_total = len(submisstions)
        context['submission_total'] = submission_total
        results = []
        
        for option in question.option_set.all():
            checked = option.pk in user_options
            percent = '{0:.2f} %'.format(count_options[option.pk] * 100 / submission_total)
            results.append((option, checked, percent))
        
        context['results'] = results
        
        return context
    