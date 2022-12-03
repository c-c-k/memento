from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('delete_question', views.delete_question, name='delete_question'),
    path('delete_choice', views.delete_choice, name='delete_choice'),
    path('repopulate', views.repopulate, name='repopulate'),
]
