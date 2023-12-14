from django.urls import path, include

from . import views

urlpatterns = [
    path('index', views.test_view, name='index'),
    path('', views.test_view0, name='home'),
    path('form', views.form_view, name='form'),
    path('login', views.log_in, name='login'),
    path('login', views.log_out, name='logout'),
    path('django/form', views.django_form, name='dform'),
    path('delete/<pk>', views.delete_item, name='delete'),
    path('edit/<pk>', views.edit_item, name='edit'),
]
