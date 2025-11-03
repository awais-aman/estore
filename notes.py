# ################ SIGNUP & LOGIN ##############################
# from django.shortcuts import render,redirect
# from django.http import HttpResponse,HttpResponseRedirect
# from .models.product import Product
# from .models.category import Category
# from .models.customer import Customer
# from django.contrib.auth.hashers import make_password, check_password
# from django.urls import reverse
# from django.views import View

# def index(request):
#     categories=Category.all_category()
#     c_id=request.GET.get('category')
#     if c_id:
#         products=Product.all_products_by_Category_id(c_id)
#     else:
#         products=Product.all_products()
#     mehr={'allproducts':products, 'categories':categories}
#     return render(request,'index.html',mehr)


# def signup(request):
#     if request.method=='GET':
#         return render(request,'signup.html')
#     else:
#         phone=request.POST.get('phone')
#         fname=request.POST.get('fname')
#         lname=request.POST.get('lname')
#         password=request.POST.get('password')
#         email=request.POST.get('email')
        
#         value={'firstname':fname,"lastname":lname,'phone':phone,'password':password,'email':email}
#         customer=Customer(first_name=fname,last_name=lname,phone=phone,email=email,password=password)
#         error_message=validatecustomer(customer)

#         if not (error_message):
#             customer.password=make_password(customer.password)
#             customer.save()
#             return redirect('login')
#         else:
#             data={'error':error_message,'values':value}
#     return render(request,'signup.html',data)


# def validatecustomer(customer):
#         error_message=None

#         if not customer.first_name:
#             error_message='''First Name Required!!!'''
#         elif len(customer.first_name)<4:
#             error_message='''First Name must be atleast of 4 chracters or more!'''
#         elif not customer.last_name:
#             error_message='''Last Name Required!!!'''
#         elif len(customer.last_name)<4:
#             error_message='''Last Name must be atleast of 4 chracters or more!'''
#         elif not customer.phone:
#             error_message='''Phone No Required!!!'''
#         elif len(customer.phone)<11:
#             error_message='''Phone No must be 10 characters.'''
#         elif not customer.password:
#             error_message='''Password Required!!!'''
#         elif len(customer.password)<=4:
#             error_message='''Password must be of altleast 10 chracters'''
#         elif len(customer.email)<5:
#             error_message='''Email must be 5 charcters long.'''
#         elif customer.isExists():
#             error_message='''Email Already Exists!!!'''
#         else:
#             pass
#         return error_message

# def login(request):
#     if request.method=='GET':
#         return render(request,'login.html')
#     else:
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         customer=Customer.check_email(email)
#         error_message=None

#         if customer:
#             flag=check_password(password,customer.password)
#             if flag:
#                 return redirect('http://127.0.0.1:8000/')
#             else:
#                 error_message='''Email or Password Invalid!!!'''
#         else:
#             error_message='''Email or Password Invalid!!!'''
#     return render(request,'login.html',{'error':error_message})

#################################################################################################################
#################################################################################################################
################################### URLS #####################################################################
'''from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="home"),
    path('signup/',views.signup, name="signup"),
    path('login/',views.login, name="login")

]
'''
###################################################################################################################
############################IMMPORTANT#######################################################
'''<td>{{x.status|default:'pending'}}</td>'''