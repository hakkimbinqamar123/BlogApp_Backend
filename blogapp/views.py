from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from blogapp.serializers import *
from .models import *
from django.db.models import Q

# Create your views here.

@csrf_exempt
def login(request):
    if request.method == 'POST':
        received_data = json.loads(request.body)
        getEmail = received_data["email"]
        getPassword = received_data["password"]

        data = list(registration.objects.filter(Q(email__exact=getEmail) & Q(password__exact=getPassword)).values())
        return HttpResponse(json.dumps(data))


@csrf_exempt
def addBlog(request):
    if request.method == 'POST':
        received_data =json.loads(request.body)
        print(received_data)
        serializer_check = BlogSerializer(data=received_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"success"}))
        else:
            return HttpResponse(json.dumps({"status":"failed"}))
        
@csrf_exempt
def view_blog(request):
    if request.method =='POST':
        blogList=blogAdd.objects.all()
        serialize_data = BlogSerializer(blogList,many=True)
        return HttpResponse(json.dumps(serialize_data.data))

@csrf_exempt
def ViewMypost(request):
    if request.method =='POST':
        received_data = json.loads(request.body)
        getUserid=received_data["userid"]
        data=list(blogAdd.objects.filter(Q(userid__icontains=getUserid)).values())
        return HttpResponse(json.dumps(data))
@csrf_exempt
def register(request):
    if request.method == 'POST':
        received_data =json.loads(request.body)
        print(received_data)
        serializer_check = PostSerializer(data=received_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"success"}))
        else:
            return HttpResponse(json.dumps({"status":"failed"}))
        

@csrf_exempt
def ViewMyprofile(request):
    if request.method =='POST':
        received_data = json.loads(request.body)
        getId=received_data["id"]
        data=list(registration.objects.filter(Q(id__exact=getId)).values())
        return HttpResponse(json.dumps(data))