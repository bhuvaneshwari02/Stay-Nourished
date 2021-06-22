from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import personal
from .models import Diet
from django.contrib.auth.forms import UserCreationForms
from django.forms import inlineformset_factory


def base(request):
    context = {'base': base}
    return render(request, "base.html", context)







def login(request):
    context = {'login': login}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request,'home1.html',context)
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
     return render(request, "login.html",context)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password2 == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email,
                                                password=password1)
                user.save()

                return redirect('login')
        else:
            messages.info(request, 'password does not match')
            return redirect('register')
    else:
        return render(request, "register.html")


def first(request):
    context = {'first': first}
    return render(request, "first.html", context)


def home1(request):
    context={'home1':home1}
    return render(request,"home1.html",context)


def about(request):
    return render(request,"about.html")


def typesofdiet(request):
    return render(request,"typesofdiet.html")


def tellusaboutyou(request):
    if request.method == 'POST':
      name = request.POST['name']
      gender = request.POST['gender']
      worktype = request.POST['worktype']
      foodhabit = request.POST['foodhabit']
      height = request.POST['height']
      weight = request.POST['weight']
      glucose = request.POST['glucose']
      bloodpressure = request.POST['blood']
      pailor=request.POST['pailor']
      bitotsspot=request.POST['spot']
      goitre=request.POST['goitre']
      pittingodema=request.POST['pitting']
      breakfast=request.POST['breakfast']
      lunch=request.POST['lunch']
      snack=request.POST['snack']
      dinner=request.POST['dinner']
      obj = personal(name=name,Gender=gender,Worktype=worktype,Foodhabit=foodhabit,Height=height,Weight=weight,Glucose=glucose,BloodPressure=bloodpressure,
                     Pailor=pailor,Bitotsspot=bitotsspot,Goitre=goitre,Pittingodema=pittingodema,Breakfast=breakfast,
                     Lunch=lunch,Snack=snack,Dinner=dinner)
      obj.save()
      if (int (glucose))==300:
          listobj = Diet.objects.get(id=1)
          return render(request, 'report.html', {'listobj': listobj})


    else:
      return render(request,"tellusaboutyou.html")


def logout (request):
    auth.logout(request)
    return render(request,"first.html")

# Create your views here.
# def index(request):
# return render (request,"index.html")
