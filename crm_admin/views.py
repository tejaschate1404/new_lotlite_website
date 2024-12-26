from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserNew
from courses_crm.models import Course
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login/')
def register_view(request):
    return render(request, 'Register.html')

@login_required(login_url='/login/')
def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        
        if password == confirm_password:
            if UserNew.objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
                return redirect('register_view')
            
            hashed_password = make_password(password)  # Hash the password
            user = UserNew(first_name=first_name, last_name=last_name, email=email, password=hashed_password)
            user.save()
            messages.success(request, "Registration successful!")
            return redirect('login_view')
        else:
            messages.error(request, "Passwords do not match.")
            return redirect('register_view')
    else:
        messages.error(request, "Invalid request method.")
        return redirect('register_view')

@csrf_exempt
def login_view(request):
    next_url = request.GET.get('next', '/courses_crm/')
    return render(request, 'login.html', {'next': next_url})

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            
            # Set session data after login
            request.session['user_id'] = user.id
            request.session['email'] = user.email
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            
            next_url = request.POST.get('next', '/courses_crm/')
            
            return redirect(next_url)
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login_view')
    else:
        messages.error(request, "Invalid request method.")
        return redirect('login_view')


@login_required(login_url='/login/')
@csrf_exempt
def courses_data(request):
    user_id = request.session.get('user_id')
    email = request.session.get('email')
    first_name = request.session.get('first_name')

    # Use the session data as needed
    courses = Course.objects.all()
    return render(request, "addcourses.html", {'courses': courses, 'first_name': first_name})

def logout_view(request):
    logout(request)
    request.session.flush()  # Clears all session data
    return redirect('/login/')
