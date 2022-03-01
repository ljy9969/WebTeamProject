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


def detail(request, question_id):
    # choice = Choice.objects.get(id=question_id)
    # context = {
    #     'choice': choice
    # }
    # return render(request, 'diagnosis/s_detail.html', context)

    question = get_object_or_404(Question, pk=question_id)

    context = {
        'my_question': question
    }
    return render(request, "diagnosis/s_detail.html", context)

    # def s_diagnosis(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # question = Question.objects.all().order_by('pub_date')
    #
    # context = {
    #     "my_question": question
    # }
    # return render(request, 'diagnosis/s_diagnosis.html', context)

    # def s_diagnosis(request, question_id):
    #     question = get_object_or_404(Question, pk=question_id)
    #     # choice = question.choice_set.get(pk=request.POST['choice'])
    #
    #     # choice.votes += 1
    #     # choice.save()
    #
    #     # question = Question.objects.all().order_by('pub_date')
    #     # choice = Choice.objects.all()
    #
    #     context = {
    #         'my_question': question,
    #         # 'my_choice': choice
    #     }

    # return render(request, 'diagnosis/s_diagnosis.html', context)
    # return HttpResponseRedirect(reverse('diagnosis:results', args=(question.id,)))


def s_result(request, question_id):
    # question = Question.objects.all().order_by('pub_date')
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'my_question': question
    }
    return render(request, 'diagnosis/s_result.html', context)
