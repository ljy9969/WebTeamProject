from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from pro_bbs.models import Question, Answer, Comment
from pro_bbs.forms import QuestionForm, AnswerForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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


@login_required(login_url='users:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('probbs:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pro_bbs/bbs_questionForm.html', context)


@login_required(login_url='users:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)  # 임시 저장을 의미
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('probbs:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pro_bbs/bbs_questionForm.html', context)


def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('probbs:detail', question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('probbs:detail', question_id=question.id)

    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pro_bbs/bbs_questionForm.html', context)


@login_required(login_url='users:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제 권한이 없습니다')
        return redirect('probbs:detail', question_id=question.id)
    question.delete()
    return redirect('probbs:index')


@login_required(login_url='users:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('probbs:detail', question_id=answer.question.id)

    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('probbs:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pro_bbs/bbs_answerForm.html', context)


@login_required(login_url='users:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('probbs:detail', question_id=answer.question.id)


@login_required(login_url='users:login')
def comment_CREATE_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            return redirect('probbs:detail', question_id=question.id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'pro_bbs/commentForm.html', context)


@login_required(login_url='users:login')
def comment_MODIFY_question(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다.')
        return redirect('probbs:detail', question_id=comment.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('probbs:detail', question_id=comment.question.id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'pro_bbs/commentForm.html', context)



@login_required(login_url='users:login')
def comment_DELETE_question(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다.')
        return redirect('probbs:detail', question_id=comment.question.id)
    else:
        comment.delete()
    return redirect('probbs:detail', question_id=comment.question.id)


@login_required(login_url='users:login')
def comment_CREATE_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect('probbs:detail', question_id=comment.answer.question.id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'pro_bbs/commentForm.html', context)


@login_required(login_url='users:login')
def comment_MODIFY_answer(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('probbs:detail', question_id=comment.answer.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('probbs:detail', question_id=comment.answer.question.id)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'pro_bbs/commentForm.html', context)


@login_required(login_url='users:login')
def comment_DELETE_answer(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('probbs:detail', question_id=comment.answer.question.id)
    else:
        comment.delete()
    return redirect('probbs:detail', question_id=comment.answer.question.id)