from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse

# Create your views here.
def home(request):
    return HttpResponse('<h1> this is my first django page</h1>')


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':question, 'error_message':"you didn't select a choice."})
    else:
        select_choice.votes +=1
        select_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



def index(request):
    latst_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latst_question_list
    }
    return render(request, 'polls/index.html', context)


