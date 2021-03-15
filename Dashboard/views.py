from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import tasks
from django.utils import timezone
from django.http import HttpResponse
import json
from django.core import serializers


class Dashboard(View):
    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            return HttpResponse("<script>window.location.href = '../';alert('User not Found!!!!!!');</script>")
        keep_objs = tasks.objects.filter(user=user, date=timezone.now().date())
        todo_objs_pen = tasks.objects.filter(user=user, RevisionDate__lt=timezone.now().date())
        todo_objs = tasks.objects.filter(user=user, RevisionDate=timezone.now().date())
        keep_lst = json.loads(str(serializers.serialize("json",keep_objs)))
        todo_lst = json.loads(str(serializers.serialize("json",todo_objs)))
        todo_lst_pen = json.loads(str(serializers.serialize("json",todo_objs_pen)))
        return render(request, 'Dashboard.html',{"keeplst":keep_lst,"todolst":todo_lst,"todolstpen":todo_lst_pen})

class AddnewView(APIView):
    def post(self,request):
        user = request.user
        if not user.is_authenticated:
            return Response("<script>window.location.href = '../';alert('User not Found!!!!!!');</script>",status=500)
        try:
            data = dict(request.data.dict())
            if data['key']=='add':
                if tasks.objects.filter(user=user, topic=data['topic'], desc=data['desc'],date=timezone.now().date()).exists():
                    return Response(data='Already exist',status=500,content_type='json')
                task_obj = tasks.objects.create(user = user)
                task_obj.topic = data['topic']
                task_obj.desc = data['desc']
                task_obj.RevisionDate = timezone.now().date() + timezone.timedelta(days=2)
                try:
                    task_obj.save()
                    data=str(task_obj.id)
                    return Response(data=data, status=200, content_type='json')
                except Exception as e:
                    return Response(data=e.__str__(),status=500)
            elif data['key']=='del':
                temp_obj = tasks.objects.get(user=user,id = data['topic'])
                try:
                    val = temp_obj.delete()
                    if val[0]==1:
                        return Response('ok')
                except Exception as e:
                    print(e.__str__())
                    return Response(e.__str__(),status=500)
            elif data['key']=='load':
                temp_obj = tasks.objects.filter(user=user,id = data['topic'])
                try:
                    data = json.loads(str(serializers.serialize("json",temp_obj)))
                    return Response(data,status=200)
                except Exception as e:
                    print(e.__str__())
                    return Response(e.__str__(),status=500)
        except Exception as e:
            print(e.__str__()+'\n\n')
            return Response(e.__str__(),status=500)

class TodoView(APIView):
    def post(self,request):
        user = request.user
        if not user.is_authenticated:
            return Response("<script>window.location.href = '../';alert('User not Found!!!!!!');</script>", status=500)
        try:
            data = dict(request.data.dict())
            print(data)
            temp = False
            if data['key'] == '1':
                temp_obj = tasks.objects.get(user=user,id = data['topicid'])
                temp_obj.marked = True
                temp = True
            elif data['key'] == '0':
                temp_obj = tasks.objects.get(user=user,id = data['topicid'])
                temp_obj.marked = False
                temp = True
            temp_obj.save()
            if temp:
                return Response('done',status=200)
            else:
                return Response('Problem',status=500)
        except Exception as e:
            print(e.__str__()+'\n\n')
            return Response(e.__str__(),status=500)

class AlltaskView(APIView):
    def get(self,request):
        user = request.user
        if not user.is_authenticated:
            return HttpResponse("<script>window.location.href = '../';alert('User not Found!!!!!!');</script>", status=500)
        alltask = tasks.objects.filter(user=user).order_by('-date')
        alltask = json.loads(str(serializers.serialize("json",alltask)))
        print(alltask)
        return render(request,"AllTask.html",{"alltask":alltask})