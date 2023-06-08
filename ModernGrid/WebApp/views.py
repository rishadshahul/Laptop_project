from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from ModernApp.models import categoryDB, productdb, ContactDB
from WebApp.models import useradmin


# Create your views here.


# -------------------------------------------------Watch Page---------------------------------------------------------------

def indexnew(req):
    data = categoryDB.objects.all()
    return render(req, "IndexWatch.html", {'data': data})


def ShopPage(req, itemcatg):
    product = productdb.objects.filter(ProductCategory=itemcatg)
    data = categoryDB.objects.all()
    return render(req, 'ShopWatch.html', {'product': product, 'data': data})


def Productpage(req, dataid):
    data = categoryDB.objects.all()
    product = productdb.objects.get(id=dataid)
    return render(req, 'productWatch.html', {'data': data, 'product': product})


def AboutPage(req):
    return render(req, 'AboutWatch.html')


def BlogPage(req):
    return render(req, 'BlogWatch.html')


def ContactPage(req):
    return render(req, 'contactWAtch.html')


def Loginpage(req):
    return render(req, 'loginWatch.html')


def Cartpage(req):
    return render(req, 'cartWatch.html')


def Login(req):
    return render(req, 'newLogin.html')


def Signup_page(req):
    if req.method == "POST":
        Username = req.POST.get('username')
        Email = req.POST.get('email')
        Password = req.POST.get('password')
        Confirmpswd = req.POST.get('confirmpswd')
        obj = useradmin(username=Username, email=Email, password=Password, confirmpswd=Confirmpswd)
        obj.save()
        return redirect(Login)

def CustomerLOgin(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r= request.POST.get('password')
        if useradmin.objects.filter(username=username_r,password=password_r).exists():
            request.session['username']=username_r
            request.session['password']=password_r
            return redirect(indexnew)
        else:
            return redirect(Login)

    return redirect(Login)

def logout(request):
    del request.session['username']
    del request.session['password']
    return  redirect(Login)


def Contactsave(req):
    if req.method=="POST":
        Message=req.POST.get('Message')
        Name=req.POST.get('ConName')
        Email=req.POST.get('ConEmail')
        Subject=req.POST.get('ConSubject')
        obj=ContactDB(message=Message, Cname=Name, Cemail=Email,Csubject=Subject)
        obj.save()
        return redirect(ContactPage)

def Contactdisplay(req):
    data=categoryDB.objects.all()
    return render(req,"ContactDisplay.html",{'data':data})

def ContactDlt(req, dataid):
    data=categoryDB.objects.filter(id=dataid)
    data.delete()
    return redirect(Contactdisplay)


