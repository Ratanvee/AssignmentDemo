from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('jobs/', views.jobs_list, name='jobs-list'),
]