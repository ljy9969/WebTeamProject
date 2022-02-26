from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from pro_bbs.models import Question, Answer


# Create your views here.


def index(request):
    question_list = Question.objects.all().order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pro_bbs/bbs_main.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pro_bbs/bbs_detail.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('probbs:detail', question_id=question.id)
