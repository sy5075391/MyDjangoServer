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
    # @action(methods=['post'], detail=False)
    # def new_person(self, request):
    #     data = json.loads(request.body)
    #     data['id'] = uuid.uuid1()
    #
    #     Person.objects.create(**data)
    #     res = {
    #         'success': True,
    #         'data': data
    #     }
    #
    #     return Response(res)
    #
    # @action(methods=['get', 'post'], detail=False)
    # def all_person(self, request):
    #     data = PersonSerializers(Person.objects.all(), many=True).data
    #     res = {
    #         'success': True,
    #         'data': data,
    #
    #     }
    #     return Response(res)

    # mixin
    queryset = Person.objects.all()
    serializer_class = PersonSerializers


def index2(request):
    article_list = Article.objects.all()

    return render(request, 'index2.html', {"list": article_list})


def mypage(request):
    return render(request, 'index.html')


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


#
from appname.serializers import UserSerializer
from appname.models import Users
from django.contrib.auth.hashers import make_password, check_password
from appname.token import create_token, verify_token


class UserViewSet(viewsets.ModelViewSet):
    # serializer_class = UserSerializer
    # queryset = Users.objects.all()
    @action(methods=['post'], detail=False)
    def register(self, request):
        data = json.loads(request.body)
        # 校验
        user = Users.objects.filter(username=data['username'])
        if len(user):
            res = {
                'success': False,
                'msg': '用户名已注册'
            }
            return Response(res)
        data['id'] = uuid.uuid1()
        data['password'] = make_password(data['password'])
        Users.objects.create(**data)
        res = {
            'success': True,
            'msg': data['password']
        }
        return Response(res)

    @action(methods=['post'], detail=False)
    def login(self, request):
        res = {
            'success': False,
            'mess': '用户名未注册'
        }
        return Response(res)
        data = json.loads(request.body)
        filter_user = Users.objects.filter(username=data['username'])
        if not len(filter_user):
            res = {
                'success': False,
                'mess': '用户名未注册'
            }
            return Response(res)
        user = UserSerializer(filter_user, many=True).data[0]
        check_pass_result = check_password(data['password'], user['password'])
        del user['password']
        if not check_pass_result:
            res = {
                'success': False,
                'mess': '密码错误'
            }
            return Response(res)

        res = {
            'success': True,
            'data': user
        }
        response = Response(res)
        response['Access-Control-Expose-Headers'] = 'auth'
        response['auth'] = create_token(user)
        return response

    @action(methods=['get'], detail=False)
    def all_users(self, request):
        # 先做登录校验，从headers拿token，如果没有HTTP_AUTH会进入except
        try:
            token = request.META.get('HTTP_AUTH')  # 从request的headers里获取token
            token = verify_token(token)  # 校验并生成新的token，如果校验失败，返回false
            if not token:
                res = {
                    'success': False,
                    'mess': '请重新登录'
                }
                return Response(res)

            users = UserSerializer(Users.objects.all(), many=True).data
            res = {
                'success': True,
                'data': users
            }
            response = Response(res)
            response['Access-Control-Expose-Headers'] = 'auth'
            response['auth'] = token
            return response
        except:
            res = {
                'success': False,
                'mess': '请登录'
            }
            return Response(res)
