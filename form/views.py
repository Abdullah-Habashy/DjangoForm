from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import user


def users(request):
    dataUser = user.objects.all()
    # receive all  users data from that model
    dataUserCount = str(dataUser.count())
    # Store users count in a variable
    data = {
        # carry all the prevoius variables inside an object
        "dataUser": dataUser,
        "dataUserCount": dataUserCount,
    }
    return render(request, 'form/users.html', data)
    # pass data to target file


def signup(request):
    # receiving data from the form inside view
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    # # checkout received data by printing
    userData = {
        "username" : username,
        "password" : password,
        "email" : email,
        "phone" : phone
    }
    print(username)
    print(email)
    print(phone)
    print(password)
    # pass data to target fields
    data = user(
        name=username,
        email=email,
        phone=phone,
        password=password,
    )
    # save data
    data.save()
    return render(request, 'form/signup.html' , userData)
