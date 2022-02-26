from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from pro_bbs.models import Question, Answer
from pro_bbs.forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator


# Create your views here.


def index(request):

    page = request.GET.get('page', '1')
    question_list = Question.objects.all().order_by('-create_date')

    # paging
    pagiantor = Paginator(question_list, 10)
    page_obj = pagiantor.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pro_bbs/bbs_main.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pro_bbs/bbs_detail.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('probbs:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pro_bbs/bbs_questionForm.html', context)


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)  # 임시 저장을 의미
            question.create_date = timezone.now()
            question.save()
            return redirect('probbs:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pro_bbs/bbs_questionForm.html', context)
