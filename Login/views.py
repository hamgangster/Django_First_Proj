from django.shortcuts import redirect,render
from .models import user
from django.db.models import Q
# Create your views here.
def check(name,phone,email):
    match = user.objects.filter(
        Q(user_name=name) &
        Q(user_phone=phone) &
        Q(user_email=email) 
    ).exists()
    return match

def index(request):
    print(request)
    pram={'Note':''}
    if request.method == "POST":
        Email = request.POST.get("Email", False)
        Name = request.POST.get("Name", False)
        Phone_num = request.POST.get("Phone", False)
        Country = request.POST.get("Con", False)

        if check(Name, Phone_num, Email):
            pram['Note']="User already exists."
            return render(request, 'Login/index.html',pram)
            
        else:
            User = user(
                user_name=Name,
                user_phone=Phone_num,
                user_email=Email,
                user_country=Country
            )
            User.save()
            request.session['is_logged_in']=True
            request.session['user_name']=Name
            request.session['user_email']=Email
            request.session['user_Phone_no']=Phone_num
            return render(request,'Login/Succesful.html')

    return render(request, 'Login/index.html')

def Login(request):
    pram={'Note':''}
    if request.method=="POST":
        Email = request.POST.get("Email", False)
        Name = request.POST.get("Name", False)
        Phone_num = request.POST.get("Phone", False)
        if check(Name, Phone_num, Email):
         request.session['is_logged_in']=True
         request.session['user_name']=Name
         request.session['user_email']=Email
         request.session['user_Phone_no']=Phone_num
         return render(request, 'Login/Succesful.html',pram)
        else:
            pram['Note']="User dose not exists."
            return render(request,'Login/Login.html',pram)
    return render(request,'Login/Login.html')

def logout(requests):
   requests.session.flush()
   return redirect('signup')