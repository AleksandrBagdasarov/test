from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question
from django.urls import reverse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'produc/index.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'produc/detail.html', {'question':question})

def result(request, question_id):
    
    response = 'You are looking at the results of questions %s'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'produc/detail.html', {
            'question' : question,
            'error_message' : 'You did not select a choice',
        })       
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('produc:results', args=(question_id,)))