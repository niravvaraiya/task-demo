from django.shortcuts import render,redirect
from django.http import HttpResponse
from shopping.models import Product,Cart,Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from shopping.forms import  CartForm,CustomerForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.mail import send_mail

# Create your views here.

def index(request):                             #main page with mail functionality without using celery 
    mobile=Product.objects.filter(category='M')
    tshirt=Product.objects.filter(category='T')
    laptop=Product.objects.filter(category='L')
    if request.method == 'POST':                # i remove my password from settings.py
        to = request.POST.get('recipient_email_address')
        send_mail('hello this is subject','this is mail  body so read it properly','varaiyaniravn@gmail.com',[to,],fail_silently=False)
        #return HttpResponse("<h1>hello</h1>")
    
    return render(request,'shop/index.html',{'mobile':mobile,'tshirt':tshirt,'laptop':laptop})
    
    

def detail(request,id):
    product=Product.objects.get(pk=id)
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            user=request.user 
            quantity=request.POST.get('quantity') 
            Cart(user=user,product=product,quantity=quantity).save()
            #return HttpResponse("<h1>hello</h1>")
            return redirect('/showcart')
    else:
        form = CartForm()
    return render(request,'shop/detail.html',{'form':form,'product':product})
    
    

def register(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponse("<p>hii nirav</p>")
    else:
        form=UserCreationForm()
    return render(request,'shop/register.html',{'form':form})

def login(request):                             #for user login functionality
    if request.method == "POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            auth_login(request,user)
            return redirect('/')
    else:
        form=AuthenticationForm()
    return render(request,'shop/login.html',{'form':form})

def search(request):                                #for search bar functionality
    if request.method == 'GET':
        search=request.GET.get('search')
        pr=Product.objects.filter(brand__iexact=search)
        #return HttpResponse("<p>hii nirav</p>")
        return render(request,'shop/search.html',{'pr':pr})

def showcart(request):                # for cart funcctionality
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
        customer=Customer.objects.filter(user=user)
        amount=0.0
        totalamount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user == user]
        print(cart_product)
        number_of_item=0
        if cart_product:
            for p in cart_product:
                temp=(p.quantity * p.product.discountprice)
                amount += temp
                number_of_item=number_of_item+1
            totalamount = amount
        print(number_of_item)
        return render(request,'shop/addtocart.html',
                      {'cart':cart,'customer':customer,'total':totalamount,'item':number_of_item}) 


def remove(request,id):
    cart=Cart.objects.get(pk=id)
    user=request.user
    if user:
        cart.delete()
    return redirect('/showcart')

def logout(request):                        #for user logout functionality
    if request.method == "POST":
        auth_logout(request)
        return redirect('/')

def profile(request):
    if request.method == "POST":
        form=CustomerForm(request.POST)
        if form.is_valid():
            user=request.user
            name=request.POST.get('name')
            locality=request.POST.get('locality')
            city=request.POST.get('city')
            zipcode=request.POST.get('zipcode')
            phone_number=request.POST.get('phone_number')
            Customer(user=user,name=name,locality=locality,city=city,zipcode=zipcode,phone_number=phone_number).save()
            return redirect("/")
    else:
        form=CustomerForm()
    return render(request,'shop/profile.html',{'form':form})



