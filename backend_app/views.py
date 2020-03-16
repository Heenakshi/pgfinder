from django.http import HttpResponse
from django.shortcuts import render, redirect
from backend_app.forms import PgUserDetailForm
from django.contrib.auth.hashers import make_password, check_password
from misc_files.generic_functions import verify_mail_send, generate_string
from backend_app.models import UserRole, PgUserDetail
from django.contrib.auth.views import auth_logout
from misc_files.authentication import authorize


def index_page(request):
    return render(request, "index.html")


def pg_registration_page(request):
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
            return redirect('/')
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
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        data = PgUserDetail.objects.filter(email=email).exists()
        if data is True:
            data = PgUserDetail.objects.get(email=email)
            if check_password(password, data.password):
                if data.is_active == 1:
                    role = data.role.role_name
                    request.session['auth'] = True
                    request.session['role'] = role
                    request.session['name'] = data.name
                    request.session['email'] = data.email
                    if role == "pg":
                        return redirect('/pg/pg_index/')
                else:
                    if data.verify_link == "":
                        string = make_password(generate_string()).replace("+", "")
                        full_link = r"127.0.0.1:8000/verify/?token={}".format(str(string))
                        update = PgUserDetail(email=email, verify_link=string)
                        update.save(update_fields=['verify_link'])
                        verify_mail_send(request.POST['email'], request.POST['name'], full_link)
                        return render(request, "login.html", {'verify_email': True})
                    else:
                        return render(request, "login.html", {'verify_email': True})
            else:
                return render(request, "login.html", {'invalid_password': True})
        else:
            return render(request, "login.html", {'invalid_email': True})
    return render(request, "login.html")


def logout(request):
    auth_logout(request)
    return redirect('/')


def update_password(request):
    try:
        auth = authorize(request.session['auth'], request.session['role'], request.session['role'])
        if auth is True:
            if request.method == "POST":
                old_password = request.POST['o_pass']
                new_password = request.POST['n_pass']
                confirm_password = request.POST['c_pass']
                if check_password(old_password, PgUserDetail.objects.get(email=request.session['email']).password):
                    if new_password == confirm_password:
                        update = PgUserDetail(email=request.session['email'], password=make_password(new_password))
                        update.save(update_fields=['password'])
                        return redirect('/pg/pg_index/')
                    else:
                        return render(request, "update_password.html", {'c_pass_match': True})
                else:
                    return render(request, "update_password.html", {'o_pass_match': True})
            return render(request, "update_password.html")
    except:
        return redirect('/')

