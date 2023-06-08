from idlelib.autocomplete import FILES

from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect

from ModernApp.models import categoryDB, productdb


# Create your views here.
def indexpage(r):
    return render(r, "indexpage.html")


def AddCategory(req):
    return render(req, "Add_Category.html")


def saveCategory(req):
    if req.method == "POST":
        na = req.POST.get('name')
        img = req.FILES['image']
        obj = categoryDB(cateName=na, cateImage=img)
        obj.save()
        return redirect(AddCategory)


def DisplayCategory(req):
    data = categoryDB.objects.all
    return render(req, 'Display_category.html', {'data': data})


def EditCategory(req, dataid):
    data = categoryDB.objects.get(id=dataid)
    print(data)
    return render(req, "Edit_Category.html", {'data': data})


def UpdateCategory(req, dataid):
    if req.method == "POST":
        na = req.POST.get("name")
        try:
            img = req.FILES["image"]
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = categoryDB.objects.get(id=dataid).cateImage
        categoryDB.objects.filter(id=dataid).update(cateName=na, cateImage=file)
        return redirect(DisplayCategory)


def deleteCategory(req, dataid):
    data = categoryDB.objects.filter(id=dataid)
    data.delete()
    return redirect(DisplayCategory)


def AddProduct(req):
    data = categoryDB.objects.all()
    return render(req, "Add_Product.html", {'data': data})


def saveProduct(req):
    if req.method == "POST":
        na = req.POST.get('name')
        ca = req.POST.get('Category')
        pr = req.POST.get('Price')
        dec = req.POST.get('Description')
        qty = req.POST.get('quantity')
        img = req.FILES['image']
        obj = productdb(ProductName=na, ProductCategory=ca, ProductPrice=pr, ProductDescription=dec, ProductQuantity=qty, ProductImage=img, )
        obj.save()
        return redirect(AddProduct)


def DisplayProduct(req):
    data = productdb.objects.all()
    return render(req, "Display_Product.html", {'data': data})


def EditProduct(req, dataid):
    data = productdb.objects.get(id=dataid)
    category_data = categoryDB.objects.all()
    print(data)
    return render(req, "Edit_Product.html", {'data': data, 'category_data': category_data})


def UpdateProduct(req, dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        ca = req.POST.get('category')
        pr = req.POST.get('Price')
        dec = req.POST.get('Description')
        qty = req.POST.get('quantity')
        try:
            img = req.FILES["image"]
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).cateImage
        productdb.objects.filter(id=dataid).update(ProductName=na,ProductCategory=ca, ProductPrice=pr, ProductDescription=dec, ProductQuantity=qty,
                                                   ProductImage=file)
        return redirect(DisplayProduct)


def DeleteProduct(req, dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(DisplayProduct)


def loginPAGE(req):
    return render(req, "LogingPage.html")



def adminlogin(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r

                return redirect(indexpage)
            else:
                return redirect(loginPAGE)
        else:
            return redirect(loginPAGE)

def Userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect (loginPAGE)




