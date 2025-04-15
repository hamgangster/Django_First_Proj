from django.http import HttpResponse
from django.shortcuts import redirect,render
import pandas as pd
import os
def check(email,phone):
    path="Data.xlsx"
    df=pd.read_excel(path)
    data_dict = df.to_dict(orient="records") 
    flag=1
    for i,content in enumerate (data_dict):
        if(content["Email"]==email or content["Phone"]==phone):
            flag=0
            break
    return flag

def log_Check(email,phone,name):
    path="Data.xlsx"
    df=pd.read_excel(path)
    data_dict = df.to_dict(orient="records") 
    flag=0
    for i,content in enumerate (data_dict):
        if(str(content["Email"]).strip()==email and str(content["Phone"]).strip()==phone and str(content["Name"]).strip()==name):            
            flag=1
            break
    return flag

def index(request):
    flag=False
    path="Data.xlsx"
    pram={'Note':""}
    Email=request.POST.get("Email",'None')
    Name=request.POST.get('Name','None')
    Phone=request.POST.get("Phone",'None')
    Country=request.POST.get("Con",'None')
    if  Email!='None' and Name!='None' and Phone!='None' and Country!='None':
     data=pd.DataFrame({
       "Name": [str(Name).strip()],
       "Email": [str(Email).strip()],
       "Phone": [str(Phone).strip()],
       "Country": [str(Country).strip()]
     })
     print(Email,Name,Phone,Country)
     if not os.path.exists(path):
        data.to_excel(path,index=False,engine="openpyxl")
        print("New Excel Creted Successfuly")
     else: 
           c_post=check(Email,Phone)
           if c_post!=0:
             with pd.ExcelWriter(path, mode="a", if_sheet_exists="overlay", engine="openpyxl") as writer:
               data.to_excel(writer, index=False, header=False, startrow=writer.sheets["Sheet1"].max_row)               
           else:
             pram["Note"]="Email Or Phone Number is Already Registered"
             return render(request,'index.html',pram)
           flag=True
    print(flag)
    if flag:
       request.session['is_logged_in']=True
       request.session['username']=Name
       return render(request,'Succesful.html')
    return render(request,'index.html',pram)

def Login(request):
   flag=False
   Email=request.POST.get("Email",'None')
   Name=request.POST.get('Name','None')
   Phone=request.POST.get("Phone",'None')
   pram={'Note':""}
   print("Login: ",Email,Name,Phone)
   if  Email!='None' and Name!='None' and Phone!='None':
      c_post=log_Check(str(Email).strip(),str(Phone).strip(),str(Name).strip())
      print(c_post)
      if c_post==1:
         request.session['is_logged_in']=True
         request.session['username']=Name
         print("This is test: ",request.session['is_logged_in'],request.session['username'])
         return render(request,'Succesful.html')
      else:
         pram["Note"]="Email,Phone Number or Name is Not Registered"
         return render(request,'Login.html',pram)

   return render(request,"Login.html")

def logout(requests):
   requests.session.flush()
   return redirect('signup')
