from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from appname.models import Article
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

import uuid
from appname import models

from django.http import HttpResponse


def index(request):
    article_list = Article.objects.all()

    return render(request, 'index.html', {"list": article_list})


def write_server(request):
    data = json.loads(request.body)
    data['id'] = uuid.uuid4()
    models.Person.objects.create(**data)
    res = {
        'success': True
    }
    return HttpResponse(json.dumps(res), content_type='application/json')


def read_server(request):
    data = serializers.serialize('python', models.Person.objects.all())
    res = {
        "success": 'True',
        'data': data
    }

    return HttpResponse(json.dumps(res, cls=DjangoJSONEncoder), content_type='application/json')
