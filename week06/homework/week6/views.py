from django.shortcuts import render

from .models import T1
from django.db.models import Avg
from django.http import HttpResponse


def comment(request):
    condtions = {'n_star__gt': 3}
    shorts = T1.objects.all()
    queryset = shorts.filter(**condtions)
    return render(request, 'result.html', locals())
