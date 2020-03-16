from django.shortcuts import render, redirect
from misc_files.authentication import authorize


def admin_index(request):
    try:
        auth = authorize(request.session['auth'], request.session['role'], "pg")
        if auth is True:
            return render(request, "admin_index.html")
    except:
        return redirect('/')

def update_password(request):
    return render(request, "update_password.html", {})