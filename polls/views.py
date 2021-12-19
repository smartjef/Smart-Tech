from django.http import HttpResponseRedirect
from polls.models import Question,Choice
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .forms import QuestionForm, ChoiceForm
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    context_object_name = 'q'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    context_object_name = 'question'

def create(request):
    if request.method == 'POST':
        q_form = QuestionForm(request.POST)
        c_form = ChoiceForm(request.POST)
        if q_form.is_valid() and c_form.is_valid:
            q_form.save()
            c_form.save()
            return redirect('polls:polls_index')
    else:
        q_form = QuestionForm()
        c_form = ChoiceForm
    context = {
        'q_form' : q_form,
        'c_form' : c_form,
    }
    return render(request, 'polls/create.html', context)

def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'q':q,
            'error_message':"You didnt select a choice",
        })
    else:
        selected_choice.voters += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:polls_results',args=(q.id,)))
        