from django.urls import path
from . import views

urlpatterns = [
    path('', views.meetings, name='meeting'),
    path('<int:id>/', views.minutes, name='minutes'),
    # path('add/', views.add, name="add_meeting_minutes")
    
    ]