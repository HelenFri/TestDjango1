from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('/home', views.index, name='home'),
    path('/', views.index, name='home'),
    path('/words_list', views.words_list, name='list'),
    path('/words_list/', views.words_list, name='list'),
    path('/add_word', views.add_word, name='add'),
    path('/add_word', views.add_word, name='add'),

]