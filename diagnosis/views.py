from django.shortcuts import render, get_object_or_404
from diagnosis.models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse


def s_diagnosis(request):
    question = Question.objects.all().order_by('pub_date')
    context = {
        'q_list': question,
    }
    return render(request, 'diagnosis/s_diagnosis.html', context)


def s_detail(request, question_id):


    question = get_object_or_404(Question, pk=question_id)
    context = {
        'my_question': question
    }
    return render(request, "diagnosis/s_detail.html", context)


def s_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice = question.choice_set.get(pk=request.POST['choice'])
    choice.votes += 1
    choice.save()

    return HttpResponseRedirect(reverse('diagnosis:s_result', args=(question.id,)))


def s_result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'my_question': question
    }
    return render(request, 'diagnosis/s_result.html', context)


# def s_result(request, question_id):
#     choice = get_object_or_404(Choice, pk=question_id)
#
#     context = {
#         'my_question': choice
#     }
#     return render(request, 'diagnosis/s_result.html', context)