from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def index(requests):
    flag = requests.session.get('is_logged_in', False)
    username = requests.session.get('username', 'Guest')
    pram={'Name':username}
    if flag:
     print(pram['Name'])   
     return render(requests,'Home/index.html',pram)
    else:
     messages.error(requests, "You need to login or sign up first.")
     return render(requests, 'index.html')
    
    