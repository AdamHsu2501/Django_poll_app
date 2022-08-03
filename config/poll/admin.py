from django.contrib import admin
from .models import Question, Option, Submission
# Register your models here.

class OptionInline(admin.StackedInline):
    model = Option
    extra = 3
    fields = ['title']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

class OptionAdmin(admin.ModelAdmin):
    fields = ['question', 'title']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Submission)