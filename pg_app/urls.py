from django.conf.urls import url
from pg_app import views

app_name = 'pg_app'

urlpatterns = [
    url('^admin_index/$', views.admin_index, name='admin_index'),
    url('^updatePass/$', views.update_password),
]

