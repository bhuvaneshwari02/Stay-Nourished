from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import personal
from .models import Diet
from .models import Food
from .models import Contact

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

def forgetpassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(email=email).exists():
            if password2 == password1:
                obj = User.objects.get(email=email)
                obj.set_password(password1)
                obj.save()
                messages.info(request, 'password reset successfully')
                return redirect('login')
            else:
                messages.info(request,'Password not match')
        else:
            messages.info(request, 'Email not exists')
            return redirect('forgetpassword')

    return render(request,'forgetpassword.html')
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


def tellusaboutyou1(request):
    return render(request,"tellusaboutyou1.html")


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
        breakfast = request.POST['breakfast']
        lunch = request.POST['lunch']
        snack = request.POST['snack']
        dinner = request.POST['dinner']

        obj = personal(name=name,Gender=gender,Worktype=worktype,Foodhabit=foodhabit,Height=height,Weight=weight,Glucose=glucose,BloodPressure=bloodpressure,
                     Pailor=pailor,Bitotsspot=bitotsspot,Goitre=goitre,Pittingodema=pittingodema,Breakfast=breakfast,
                     Lunch=lunch,Snack=snack,Dinner=dinner)
        obj.save()
        bmi = round(int(weight) / ((int(height)/100) * (int(height)/100)))
        glucose = int(glucose)
        bloodpressure = int(bloodpressure)
        pailor = pailor
        bitotsspot = bitotsspot
        goitre = goitre
        pittingodema = pittingodema




        if(int(glucose)==300 and int(bloodpressure)==14090 and (foodhabit)=='Vegetarian'):
             list = Diet.objects.get(id=6)
             return render(request, 'report.html',{'bmi':bmi,'list':list,'glucose': glucose,'bloodpressure':bloodpressure,'pailor':pailor,})
        if(int(glucose)==300 and int(bloodpressure)==14090 and (foodhabit)=='Non-Veg'):
             list = Diet.objects.get(id=7)
             return render(request, 'report.html', {'bmi': bmi, 'list': list, 'glucose': glucose,'bloodpressure':bloodpressure,'pailor':pailor,})
        if int(glucose) == 300 and (foodhabit) == 'Vegetarian':
            list = Diet.objects.get(id=1)
            return render(request, 'report.html',
                          {'bmi': bmi, 'list': list, 'glucose': glucose, 'bloodpressure': bloodpressure, 'pailor':pailor})
        if int(glucose) == 300 and (foodhabit) == 'Non-Veg':
            list = Diet.objects.get(id=8)
            return render(request, 'report.html',
                          {'bmi': bmi, 'list': list, 'glucose': glucose, 'bloodpressure': bloodpressure,'pailor':pailor})
        if int(weight)<20 and (foodhabit) =='Non-veg':
             list = Diet.objects.get(id=9)
             return render(request,'report.html',{'bmi': bmi, 'list': list ,'glucose': glucose,'bloodpressure':bloodpressure,'pailor':pailor})
        if pailor == 'Yes':
            list = Diet.objects.get(id=11)
            return render(request, 'report.html',
                          {'bmi': bmi, 'list': list, 'glucose': glucose, 'bloodpressure': bloodpressure,'pailor':pailor})
        if goitre == 'Yes' and (foodhabit) =='Vegetarian':
            list = Diet.objects.get(id=20)
            return render(request, 'report.html',
                          {'bmi': bmi, 'list': list, 'glucose': glucose, 'bloodpressure': bloodpressure,
                           'pailor': pailor,'goitre': goitre})

        if goitre == 'Yes' and (foodhabit) == 'Non-veg':
            list = Diet.objects.get(id=21)
            return render(request, 'report.html',
                          {'bmi': bmi, 'list': list, 'glucose': glucose, 'bloodpressure': bloodpressure,
                           'pailor': pailor, 'goitre': goitre})
        if pittingodema == 'Yes':
            list = Diet.objects.get(id=21)
            return render(request, 'report.html',
                          {'bmi': bmi, 'list': list, 'glucose': glucose, 'bloodpressure': bloodpressure,
                           'pailor': pailor, 'goitre': goitre,'pittingodema' : pittingodema})
        if bitotsspot == 'Yes' and (foodhabit) =='Vegetarian':
            list = Diet.objects.get(id=13)
            return render(request, 'report.html',
                          {'bmi': bmi, 'list': list, 'glucose': glucose, 'bloodpressure': bloodpressure,
                           'pailor': pailor, 'goitre': goitre, 'pittingodema': pittingodema, 'bitotsspot' : bitotsspot})

        if bitotsspot == 'Yes' and (foodhabit) =='Non-veg':
            list = Diet.objects.get(id=13)
            return render(request, 'report.html',
                          {'bmi': bmi, 'list': list, 'glucose': glucose, 'bloodpressure': bloodpressure,
                           'pailor': pailor, 'goitre': goitre, 'pittingodema': pittingodema, 'bitotsspot' : bitotsspot})
        if (int(bmi)>25):
            list = Diet.objects.get(id=5)
            return render(request, 'report.html',
                          {'bmi': bmi, 'list': list, 'glucose': glucose, 'bloodpressure': bloodpressure,
                           'pailor': pailor, 'goitre': goitre, 'pittingodema': pittingodema, 'bitotsspot' : bitotsspot})
        if (int(bmi)<19):
            list= Diet.objects.get(id=5)
            return render(request, 'report.html',
                          {'bmi': bmi, 'list': list, 'glucose': glucose, 'bloodpressure': bloodpressure,
                           'pailor': pailor, 'goitre': goitre, 'pittingodema': pittingodema, 'bitotsspot' : bitotsspot})

        else:
            list = Diet.objects.get(id=12)
            return render(request, 'report.html', {'bmi': bmi, 'list': list,'glucose': glucose ,'bloodpressure':bloodpressure,'pailor':pailor})

    else:
        return render(request,"tellusaboutyou.html")

def knowyourfoods(request):
    if request.method =='POST':
       name = request.POST['searches'].lower()
       listobj = Food.objects.get(Nameofthefood=name)
       return render(request, 'knowyourfoods.html', {'listobj': listobj})

    return render(request,'knowyourfoods.html')


def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        text = request.POST['query']
        obj = Contact(Name=name,Email=email,Phone=int(phone),Query=text)
        obj.save()
        messages.info(request,'Your Query has been successfully registered!')
        return render(request,"contactus.html")

    return render(request,"contactus.html")



def gallery(request):
    return render(request,"gallery.html")


def logout (request):
    auth.logout(request)
    return render(request,"first.html")



# Create your views here.
# def index(request):
# return render (request,"index.html")
