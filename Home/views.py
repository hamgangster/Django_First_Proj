from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def index(requests):
    flag = requests.session.get('is_logged_in', False)
    username = requests.session.get('user_name', 'Guest')
    user_email = requests.session.get('user_email', 'Guest')
    user_phone = requests.session.get('user_Phone_no', 'Guest')
    pram={'Name':username}
    if flag:
     print(pram['Name'])   
     return render(requests,'Home/index.html',pram)
    else:
     messages.error(requests, "You need to login or sign up first.")
     return render(requests, 'index.html')

def About(requests):
    flag = requests.session.get('is_logged_in', False)
    if flag:   
     return render(requests,'Home/About.html')
    else:
     messages.error(requests, "You need to login or sign up first.")
     return render(requests, 'index.html')
    
    