from django.shortcuts import render, HttpResponse, redirect
from . models import StudentDetail
from django.contrib.auth import authenticate, login, logout
import datetime
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

from .forms import TestForm


def test_view(request):
    data = [{'name': 'ram', 'address': 'ktm'},
            {'name': 'hari', 'address': 'ctw'},
            {'name': 'shyam', 'address': 'htd'}]
    return render(request, 'app1/index.html', {'data': data})


def test_view0(request):
    stu = StudentDetail.objects.all()
    return render(request, 'app1/home.html', {'students': stu})


def form_view(request):
    if request.method == 'POST':
        error_msg = []
        email1 = request.POST['email']
        password1 = request.POST['password']
        address1 = request.POST['address']

        if not email1:
            error_msg.append('Email cannot be blank')
        if not password1:
            error_msg.append('Please enter password')
        if error_msg:
            messages.error(request, error_msg)

        user = User.objects.first()

        StudentDetail.objects.create(email=email1, password=password1,
                                     address=address1, created_by=user, created_at=datetime.datetime.now())
        messages.success(request, "Data saved successfully")

    return render(request, 'app1/form.html')


def log_in(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']

        user = authenticate(username=username1, password=password1)

        if user:
            login(request, user)
            return redirect('home')
        else:
            logout(request)
            return redirect('login')
    return render(request, 'app1/login.html')


def log_out(request):
    logout(request)
    return redirect('login')


def edit_item(request, pk):
    students = StudentDetail.objects.get(id=pk)
    if request.method == 'POST':
        email1 = request.POST.get('email')
        password1 = request.POST['password']

        StudentDetail.objects.filter(id=pk).update(
            email=email1, password=password1)
        return redirect('home')
    return render(request, 'app1/edit.html', {'edit_student': students})


def delete_item(request, pk):
    students = StudentDetail.objects.get(referrence_id=pk)
    students.is_delete = True
    students.save()
    return redirect('home')


def django_form(request, pk):
    if request.method == "POST":
        data = TestForm(request.POST)
        if data.is_valid():
            name = data.cleaned_data['name']
            email = data.cleaned_data['email']
            password = data.cleaned_data['password']
            print(data.cleaned_data)
    else:
        fn = TestForm()
        return render(request, 'app1/django_form.html', {'form': fn})
