import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from probbs.models import Question, Comment
from django.contrib import messages
from probbs.forms import QuestionForm
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.db.models import Q


# Create your views here.


def index(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')

    question = Question.objects.order_by('-create_date')
    if kw:
        question = question.filter(
            Q(title__icontains=kw) |
            Q(content__icontains=kw) |
            Q(author__username__icontains=kw)
        ).distinct()
    paginator = Paginator(question, 10)
    page_obj = paginator.get_page(page)
    context = {
        'question_list': page_obj,
        'page': page,
        'kw': kw
    }
    return render(request, 'probbs/bbs_main.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    comment = Comment.objects.filter(post=question_id).order_by('-create_date')
    comment_count = comment.exclude(deleted=True).count()

    question.views += 1
    question.save()

    if request.user == question.author:
        question_auth = True
    else:
        question_auth = False

    context = {
        'question': question,
        'question_auth': question_auth,
        'comment_count': comment_count,
        'comments': comment,
    }
    return render(request, 'probbs/bbs_detail.html', context)


@login_required(login_url='users:login')
@permission_required('can_create_doctor', login_url=reverse_lazy('probbs:index'))
def create_comment(request, question_id):
    post = get_object_or_404(Question, id=question_id)
    author = request.POST.get('author')
    content = request.POST.get('content')
    if content:
        comment = Comment.objects.create(post=post, content=content, author=request.user)
        comment_count = Comment.objects.filter(post=question_id).exclude(deleted=True).count()
        post.comments = comment_count
        post.save()
        data = {
            'author': author,
            'content': content,
            'created': '방금 전',
            'comment_count': comment_count,
            'comment_id': comment.id
        }
        if request.user == post.author:
            data['self_comment'] = '(작성자)'

        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type="application/json")


@login_required(login_url='users:login')
def delete_comment(request, question_id):
    post = get_object_or_404(Question, id=question_id)
    comment_id = request.POST.get('comment_id')
    target_comment = Comment.objects.get(pk=comment_id)

    if request.user == target_comment.author:
        target_comment.deleted = True
        target_comment.save()
        comment_count = Comment.objects.filter(post=question_id).exclude(deleted=True).count()
        post.comments = comment_count
        post.save()
        data = {
            'comment_id': comment_id,
            'comment_count': comment_count,
        }
        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type='application/json')


@login_required(login_url='users:login')
# @permission_required('can_create_doctor', login_url=reverse_lazy('probbs:index'))
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('probbs:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'probbs/bbs_form.html', context)


@login_required(login_url='users:login')
def modify_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('probbs:detail')

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('probbs:detail', question_id=question.id)
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'probbs/bbs_form.html', context)


@login_required(login_url='users:login')
def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('probbs:detail', question_id=question.id)
    question.delete()
    return redirect('probbs:index')


@login_required(login_url='users:login')
def like_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        question.question_like_count.add(request.user)
    return redirect('probbs:detail', question_id=question.id)
