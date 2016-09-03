# -*- coding:UTF-8 -*-
import json
from django.shortcuts import render
from django.views.decorators.gzip import gzip_page
from maillist.models import PhoneNumber
from django.http import HttpResponse


def test(request):
    return render(request, 'test.html')


@gzip_page
def synchro(request):
    contacts = PhoneNumber.objects.filter(user_id=request.POST.dict().get('user_id')).order_by('info_id', 'name').values('info_id', 'name', 'phone')
    contacts = [contact for contact in contacts]
    return HttpResponse(json.dumps({'contacts': contacts}), content_type="application/json")
