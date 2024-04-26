from django.urls import path
from . import views


app_name = "app_todo"

urlpatterns = [
    path("" , views.home , name="home"),
    path("add" , views.add_mission , name="add_mission"),
    path("done/<int:id>" , views.done , name="done"),
    path("signup" , views.user_signup.as_view() , name= "user_signup"),
    path('accounts/profile/' , views.user_redirect_home , name='redirect_home'),
    
]
