from django.shortcuts import render , redirect
from django.urls import reverse , reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from . import models
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


# Create your views here.
@login_required(login_url="/login")
def home(request):

    current_time = datetime.datetime.now()
    all_missions = models.mission.objects.filter(is_done = False).filter(username = request.user.username).order_by("-added_at").all()
    all_missions_asc = models.mission.objects.filter(is_done = False).filter(username = request.user.username).order_by("added_at").all()

    for mission_item in all_missions_asc:
        current_datetime = datetime.date(year=current_time.year , month=current_time.month , day=current_time.day)
        mission_datetime = datetime.date(year=mission_item.added_at.year , month=mission_item.added_at.month , day=mission_item.added_at.day)
        #print((current_datetime - mission_datetime).days)
        mission_item.remained_days = mission_item.time - (current_datetime - mission_datetime).days
        mission_item.save()
    
    return render(request, 'app_todo/list.html' , context={"missions": all_missions , 'current_time':current_time })


@login_required(login_url= "/login")
def add_mission(request):
    
    time_value_list = list(range(1,16))
    if request.method == "POST":
        title_input = request.POST["title"]
        index_input = request.POST["mission_index"]
        time_input = request.POST["mission_time"]

        current_user = request.user.username
        model_for_save = models.mission(title = title_input, index = index_input , time = time_input , username = current_user)
        model_for_save.save()
        return redirect(reverse("app_todo:home"))
    
    else:
        return render(request , "app_todo/add_mission.html" , context= {'time_value_list' : time_value_list })


def done(request , id): 
    print(models.mission.objects.get(pk=id))
    done_mission = models.mission.objects.get(pk=id)
    done_mission.is_done = True
    done_mission.save()
    return redirect("app_todo:home")




class user_signup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"


def user_logout(request):
    logout(request)

def user_redirect_home(request):
    return redirect(reverse('app_todo:home'))

