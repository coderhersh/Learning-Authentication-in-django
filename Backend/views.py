from django.shortcuts import render
from Backend.models import User
from django.contrib.auth.models import User, auth

def signin(request):
    if request.method == 'POST':
        entered_username = request.POST['user_name']
        entered_password = request.POST['password']
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        entered_username = request.POST['user_name']
        entered_firstname = request.POST['first_name']
        entered_lastname = request.POST['last_name']
        entered_email = request.POST['email']
        entered_password = request.POST['password']
        entered_confirmed_password = request.POST['confirm_password']

        User(email=entered_email, user_id=entered_username, 
        first_name=entered_firstname, last_name=entered_lastname,
        password=entered_password).save()

        print(entered_email, entered_firstname, entered_lastname, entered_email
        , entered_password)

    return render(request, 'signup.html')

def result(request):
    return render(request, 'result.html')
