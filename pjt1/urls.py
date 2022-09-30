from unicodedata import name
from django.urls import path
from . import views

app_name = 'pjt1'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('edit/<int:pk>', views.edit, name = 'edit'),
    path('edit_method/<int:pk>', views.edit_method, name = 'edit_method')

]