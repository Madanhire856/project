from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Register, Houses, Payments, Notices
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime


def register(request):
    error_message = None
    success_message = None
    user = Register()
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm']
        if any(char.isdigit() for char in first_name):
            error_message = "name must not contain digits"
        elif any(char.isdigit() for char in last_name):
            error_message = "name must not contain digits"
        elif any(char.isdigit() for char in gender):
            error_message = "gender must not contain digits"
        elif confirm_password != password:
            error_message = "Passwords didn't match"

        else:
            hashed_password = make_password(confirm_password)

            user = Register(first_name=first_name, last_name=last_name, gender=gender, email=email,
                            password=hashed_password)

            user.save()
            success_message = "Registration successful"

    return render(request, 'register.html', context={'error': error_message, 'success': success_message})

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html', context={})
def login(request):
    error_message = None

    if request.method == "POST":
        user_email = request.POST['email']
        user_password = request.POST['password']
        user = Register.objects.get(email=user_email)
        if check_password(user_password, user.password):
            return redirect('dashboard')
        else:
            error_message = 'Invalid login'
    return render(request, 'login.html', context={'error_message': error_message})


@login_required(login_url='/registration/login/')
def dashboard(request):
    return render(request, 'dashboard.html', context={})


def add_house(request):
    error_message = None
    success_message = None

    if request.method == 'POST':

        number = request.POST['number']
        name = request.POST['name']
        surname = request.POST['surname']
        gender = request.POST['gender']
        phone = request.POST['phone']
        houses = Houses.objects.filter(number=number)

        if any(char.isdigit() for char in name):
            error_message = 'Name does not accept numbers'
        elif any(char.isdigit() for char in surname):
            error_message = 'Surname does not accept numbers'
        elif any(char.isalpha() for char in phone):
            error_message = 'Invalid phone number'

        elif len(phone) < 10:
            error_message = 'Invalid phone number'

        else:

            if houses:
                error_message = "House number already exist"
            else:

                houses = Houses(number=number, name=name, surname=surname, gender=gender, phone=phone)
                houses.save()
                success_message = "House successfully added "

    return render(request, 'add_house.html',
                  context={'error_message': error_message, 'success_message': success_message})


def payments(request):
    error_message = None
    success_message = None
    if request.method == 'POST':
        number = request.POST['number']
        month = request.POST['month']
        amount = request.POST['amount']
        facilitator = request.POST['facilitator']

        if any(char.isalpha() for char in number):
            error_message = "Invalid house number"
        elif any(char.isalpha() for char in amount):
            error_message = "Invalid amount"
        elif any(char.isdigit() for char in facilitator):
            error_message = "Invalid name of facilitator"

        else:

            verify_number = Houses.objects.filter(number=number)
            payments = Payments()

            if verify_number:
                payments = Payments(number=number, month=month, amount=amount, facilitator=facilitator)
                payments.save()
                success_message = "Payment recorded successfully"
            else:
                error_message = "House number does not exist"
    return render(request, 'payments.html',
                  context={'error_message': error_message, 'success_message': success_message})


def post_notice(request):
    error_message = None
    success_message = None
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        notice = Notices()

        notice = Notices(title=title, content=content)
        notice.save()

        success_message = 'Notice posted successfully'

    return render(request, 'post_notice.html', context={'success_message': success_message})


def notices(request):
    notices = Notices.objects.all()

    return render(request, 'notices.html', context={'notices': notices})


def display_payments(request):
    house = None

    if request.method == "POST":
        selected_month = request.POST['month']

        house = Payments.objects.filter(month=selected_month)

    return render(request, 'display_payments.html', context={'house': house})
