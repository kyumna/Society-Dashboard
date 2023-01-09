from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('excom/', views.admin, name='excom'),
    path('director/', views.customer, name='director'),
    path('member/', views.employee, name='member'),
    # path('edit/', views.edit, name='edit profile'),
    path('register/', views.register, name='register'),
    path('member_details/', views.member_details, name= 'member_details'),
    path('add_minutes/', views.add, name="add_meeting_minutes"),
    path("schedule/", views.scheduleMeeting, name="schedule_meeting"),



]