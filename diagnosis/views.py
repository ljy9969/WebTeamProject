from django.shortcuts import render, get_object_or_404, redirect
from diagnosis.models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages


def s_diagnosis(request):
    question = Question.objects.all().order_by('pub_date')
    choice = Choice.objects.filter(Q(choice_text='내용'))
    context = {
        'q_list': question,
        'c_list': choice
    }
    return render(request, 'diagnosis/main1.html', context)


def my_views(request):
    if request.method == 'POST':
        select_list = []
        for i in range(8):
            selected = request.POST.get('selected' + str(i))
            if selected is None:
                continue
            else:
                select_list.append(int(selected))

        result = sum(select_list)

        if len(select_list) != 8:
            messages.warning(request, '선택지를 모두 제출해 주세요.')
            return render(request, 'diagnosis/main2.html')

        else:
            if result < 4:
                messages.warning(request, '{} 표 입니다. 코로나가 의심되지 않지만 조심하세요. 5초 뒤 "코로나 증상 및 행동수칙" 페이지로 이동합니다.'.format(result))
                return render(request, 'diagnosis/main3.html')

            elif 4 <= result or result == 8:
                messages.warning(request, '{} 표 입니다. 코로나가 의심되오니 즉시 선별검사소나 병원을 방문하세요. 5초 뒤 "전문의에게 물어보세요" 페이지로 이동합니다.'.format(result))
                return render(request, 'diagnosis/main1.html')

            # elif result == 8:
            #     messages.warning(request, '{} 표 입니다. 코로나가 의심되오니 즉시 선별검사소나 병원을 방문하세요. 5초 뒤 "전문의에게 물어보세요" 페이지로 이동합니다.'.format(result))
            #     return render(request, 'diagnosis/main1.html')