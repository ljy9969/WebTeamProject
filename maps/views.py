from django.shortcuts import render

# Create your views here.

#
# f = open("/maps/static/csv/data_hospital.csv",
#          'r', encoding='cp949')
# l = []
# lines = f.readlines()
# for line in lines:
#     l.append(line.split(','))
# f.close()
#
# data = l[:]
# print(data)


def pos_hospital(request):
    # alldata = Post.objects.all()

    return render(request, 'maps/positions.html')
                  # {'data': data})
