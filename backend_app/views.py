from django.http import HttpResponse
from django.shortcuts import render, redirect
from backend_app.forms import PgUserDetailForm
from django.contrib.auth.hashers import make_password
from misc_files.generic_functions import verify_mail_send, generate_string
from backend_app.models import UserRole, PgUserDetail


def index_page(request):
    return render(request, "index.html")


def registration_page(request):
    if request.method == "POST":
        data = UserRole.objects.get(role_name='pg').role_id
        role_form = PgUserDetailForm(request.POST)
        if role_form.is_valid():
            form = role_form.save(commit=False)
            form.role_id = data
            form.name = request.POST['name']
            form.email = request.POST['email']
            form.password = make_password(request.POST['password'])
            form.address = request.POST['gender']
            form.mobile = request.POST['mobile']
            string = make_password(generate_string()).replace("+", "")
            full_link = r"127.0.0.1:8000/verify/?token={}".format(str(string))
            form.verify_link = string
            form.save()
            verify_mail_send(request.POST['email'], request.POST['name'], full_link)
            return HttpResponse("<h1>Sucessfully Saved</h1>")
        else:
            return HttpResponse("<h1>Form is not valid</h1>")
    return render(request, "registration.html")



def verify_link(request):
    try:
         token = request.GET['token']
    except Exception as error:
         return HttpResponse("Invalid {}".format(error))
    else:
        data = PgUserDetail.objects.filter(verify_link=token).exists()
        if data is True:
            update = PgUserDetail(email=PgUserDetail.objects.get(verify_link=token).email, verify_link="", is_active=1)
            update.save(update_fields=['verify_link', 'is_active'])
            return redirect("/login/")
        else:
            return HttpResponse("Invalid Token")


def login_page(request):
    return render(request, "login.html")
