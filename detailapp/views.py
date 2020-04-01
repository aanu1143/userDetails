from django.shortcuts import render
from django.http import HttpResponse
from detailapp.models import *
from django.template import loader


def index(request):
    user_detail_list = UserDetails.objects.order_by('-id')[:5]
    template = loader.get_template('detailapp/view_web.html')
    context = {
        'user_detail_list': user_detail_list,
    }
    return HttpResponse(template.render(context, request))
