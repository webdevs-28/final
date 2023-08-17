from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from devblogs.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.

# basics
def home(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        return render(request,'home/home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        phone= request.POST.get('phone')
        if len(name) == 0:
            messages.error(request,"plese enter a name")
        elif len(email) == 0:
            messages.error(request,'')
        elif "." not in email:
            messages.error(request,"plese enter a valid email")
        elif len(phone) >= 16 or len(phone) <=9:
            messages.error(request,"please enter a valid phone number")
        # elif  phone is  int():
        #     messages.error(request,"please enter a valid phone number")
        else:
            cont = Contact(name=name,email=email,phone=phone,content=content)
            cont.save()
            messages.success(request,"your message has been submitted")
            
        print("we are using post request")
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')

def blog(request):
    return HttpResponse("fhthtrh")

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allposts = Post.objects.none
    else:
        allpoststitle = Post.objects.filter(title__icontains=query)
        allpostscontent = Post.objects.filter(content__icontains=query)
        allposts = allpoststitle.union(allpostscontent)
        
    params = {'allposts':allposts,'query':query}
    return render(request,'home/search.html',params)
    # return HttpResponse("this is search")
    
# auth API's
def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"you are logged in successfully")
            return redirect("/")
        elif user is None:
            messages.error(request,"Please enter correct information")
            return redirect("/")
    return render(request,'home/login.html')

def logoutuser(request):
    return render(request,'home/logout.html')
    logout(request)
    messages.success(request,"logged out successfully")
    return redirect("/")

def logoutuserfn(request):
    logout(request)
    messages.success(request,"You are logged out successfully")
    return redirect("/")

def signupuser(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordcon = request.POST.get('passwordcon')
        user = User.objects.create_user(username=name,email=email,password=password)
            
        if password != passwordcon:
            messages.error(request,"please enter correct the password")
        else:
            messages.success(request,"signed up successfully")
            user.save()
            return redirect("/")
    return render(request,'home/signup.html')
