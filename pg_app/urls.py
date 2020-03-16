from django.conf.urls import url
from pg_app import views

app_name = 'pg_app'

urlpatterns = [
    url('^pg_index/$', views.pg_index, name='pg_index'),
]