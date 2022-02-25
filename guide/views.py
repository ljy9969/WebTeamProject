from django.shortcuts import render

def guide(request):
    return render(request, 'guide/guide.html')
