# from urllib import response
from django.shortcuts import render,redirect,reverse
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.views.decorators.cache import never_cache


# Create your views here.
user='aisw'
passw='1234'

def login_user(request):
    if 'username' in request.session:
        if 'username' in request.COOKIES:
            if request.session['username']==request.COOKIES['username']:
                return redirect(home)

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        # user = authenticate(username=username,password=password)
        
        
        response=redirect('home')
        # if user is not None:
        if username==user and password==passw:
            response.set_cookie('username',username)
            request.session['username']=username
            
            return response
        else:
            return render(request,'login/login.html',{'error_msg':"Invalid Credentials"})
    return render(request,'login/login.html')



def home(request):
    if 'username' in request.session  and 'username' in request.COOKIES :
        
        return render(request,'login/home.html',{'username':user})
    return redirect(login_user)




def logout_user(request):
    response=HttpResponseRedirect(reverse('login'))

    request.session.flush()
    response.delete_cookie('username')
    return response