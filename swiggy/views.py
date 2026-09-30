
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import task
from django.contrib.auth.models import User 
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def home(request):
    return HttpResponse("<h1>menu</h1>")


def first(request):
    return render(request,'login.html')

def second(request):
    return render(request,'page2.html')

def third(request):
    return render(request,'page3.html')

def fourth(request):
    return render(request,'page4.html')




def page(request):
    if request.method =='GET':
       return render(request,'page1.html')
    elif request.method =='POST':
        print(request.POST)
        data=request.POST
        num= data.get('number',0)
    return render(request, 'page1.html', context={'nums': int(num), 'number':list(range(1,int(num) ))})


def third(request):
    all_tasks = task.objects.all()
    if request.method=='GET':
        return render(request,'page3.html', context={'tasks': all_tasks})
    elif request.method=='POST':
        data=request.POST

        task_name = data.get('task_name')
        due_date = data.get('due_date')
        new_task = task.objects.create(task_name=task_name, due_date=due_date)
        new_task.save()
        return render(request,'page3.html', context={'tasks': all_tasks})


def fourth(request):
    if request.method=='GET':
        return render( request,'page4.html')
    if request.method=='POST':
        data=request.POST
        username=data.get('email')
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        password=data.get('password') 
        if len(first_name)<=1:
            return render(request,'page4.html',context={'error':'first num cannot be 1 letter'})   
        new_user= User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        new_user.set_password(password)
        new_user.save()
        return render(request,'first.html')



def first(request):
    if request.method=='GET':
        return render(request,'login.html')
    if request.method=='POST':
        data=request.POST
        username=data.get('email')
        password=data.get('password')
          
        print(data)
        t_user=User.objects.filter(username=username)
        print(t_user)
        if len(t_user)==0:
            return render(request,'login.html' , context={'error':'user not found'})
        t_user=t_user[0]
        valid=t_user.check_password('password')
        if not valid:
            return render (request,'page4.html', context={'error': 'invalid password'})
        
        login(request, t_user)
        return redirect('menu')



    
def console(request):
    return render(request,'console.html')


def calculator(request):
    return render(request,'calculator.html')




def net(request):
    task_name=task.objects.all().values()
    return JsonResponse({'use0'
    ''
    'rs':list(task_name)})



@csrf_exempt
def recv_task(request):
    if request.method =="POST":
        data=request.body.decode('utf-8')
        data=json.loads(data)
        task.objects.all()
        # task_name=data[task_name]
        new=task.objects.create(task_name=data["task_name"],due_date=data['due_date'])
        new.save()
        print(data,"........")
        return JsonResponse({"status":"ok"})


@csrf_exempt
def task_delete(request):
    if request.method =="DELETE":
        params=request.GET
        task_id=params.get('task_id')
        if task_id is None:
            return JsonResponse({"status":"task_id is required"})
        objs=task.objects.filter(id=task_id)
        objs.delete()
        return JsonResponse({"status":"ok"})
    else:
        return JsonResponse({"status":"method not allowed"})

@csrf_exempt
def is_put(request):
    if request.method =="PUT":
       params=request.GET
       task_id=params.get("task_id")
       if task_id is None:
           return JsonResponse({"status":"task_id is required"})
       objs=task.objects.filter(id=task_id)
    if len(objs)<1 :
                return JsonResponse({"status":"ok"},status=400)
    obj=objs[0]
    obj.is_completed=not obj.is_completed
    obj.save()
    return JsonResponse({"status":"ok"})


