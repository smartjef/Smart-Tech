from django.forms import ModelForm

from .models import Question,Choice

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text',]



class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['question','choice_text',]    