from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from appname.models import Article
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

import uuid
from appname import models
from appname.models import Person

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from appname.serializers import PersonSerializers


# restfulAPI method one
class Test(APIView):
    def get(self, request):
        a = request.GET['a']
        res = {
            'success': True,
            'data': a
        }
        return Response(res)


# restfulAPI method two


class PersonViewSet(viewsets.ModelViewSet):
    @action(methods=['post'], detail=False)
    def new_person(self, request):
        data = json.loads(request.body)
        data['id'] = uuid.uuid1()

        Person.objects.create(**data)
        res = {
            'success': True,
            'data': data
        }

        return Response(res)

    @action(methods=['get'], detail=False)
    def all_person(self, request):
        data = PersonSerializers(Person.objects.all(), many=True).data
        res = {
            'success': True,
            'data': data
        }
        return Response(res)


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
