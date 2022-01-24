from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cats/<int:cat_id>', views.categories, name='categories'),
]