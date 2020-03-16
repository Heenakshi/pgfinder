from django.shortcuts import render, redirect
from misc_files.authentication import authorize


def pg_index(request):
    try:
        auth = authorize(request.session['auth'], request.session['role'], "pg")
        if auth is True:
            return render(request, "pg_index.html")
    except:
        return redirect('/')
