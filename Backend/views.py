from django.shortcuts import redirect, render
from Backend.models import User
from django.contrib import messages
from django.contrib.auth.models import User, auth

def signin(request):
    if request.method == 'POST':
        entered_username = request.POST['user_name']
        entered_password = request.POST['password']

        user = auth.authenticate(username=entered_username, password=entered_password)

        if user is not None:
            auth.login(request, user)
        else:
            messages.info(request, 'You have entered wrong credentials!!!')
            redirect('/')
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        entered_username = request.POST['user_name']
        entered_firstname = request.POST['first_name']
        entered_lastname = request.POST['last_name']
        entered_email = request.POST['email']
        entered_password = request.POST['password']
        entered_confirmed_password = request.POST['confirm_password']

        if entered_password == entered_confirmed_password:
            if User.objects.filter(email=entered_email).exists() == False:
                if User.objects.filter(user_id=entered_username).exists() == False:        
                    User(email=entered_email, user_id=entered_username, 
                    first_name=entered_firstname, last_name=entered_lastname,
                    password=entered_password).save()
                else:
                    messages.info(request, 'Username already exists!!!')
            else:
                messages.info(request, 'Email antered already exists!!')
        else:
            messages.info(request, 'Password is not matching!!')

            
        print(entered_email, entered_firstname, entered_lastname, entered_email
        , entered_password)

    return render(request, 'signup.html')

def result(request):
    return render(request, 'result.html')
