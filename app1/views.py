from django.shortcuts import render, HttpResponse, redirect
from . models import StudentDetail
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def test_view(request):
    data = [{'name': 'ram', 'address': 'ktm'},
            {'name': 'hari', 'address': 'ctw'},
            {'name': 'shyam', 'address': 'htd'}]
    return render(request, 'app1/index.html', {'data': data})


def test_view0(request):
    student = StudentDetail.objects.all()
    return render(request, 'app1/home.html', {'students': student})


def form_view(request):
    if request.method == 'POST':
        email1 = request.POST.get('email')
        password1 = request.POST['password']
        address1 = request.POST.get('address')

        StudentDetail.objects.create(
            email=email1, password=password1, address=address1)
        return redirect('login')

    return render(request, 'app1/form.html')


def log_in(request):
    if request.method == 'POST':
        email1 = request.POST['email']
        password1 = request.POST['password']

        user = authenticate(email=email1, password=password1)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'app1/login.html')


def edit_item(request, pk):
    if request.method == 'POST':
        email1 = request.POST.get('email')
        password1 = request.POST['password']

        StudentDetail.objects.filter(id=pk).update(
            email=email1, password=password1)
        return redirect('home')
    students = StudentDetail.objects.get(id=pk)
    return render(request, 'app1/edit.html', {'edit_student': students})


def delete_item(request, pk):
    StudentDetail.objects.get(id=pk).delete()
    return redirect('home')
