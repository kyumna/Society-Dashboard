from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login
from account.models import  User, Members
from meeting_minutes.models import  meeting, schedule
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.contrib.auth import get_user_model
User = get_user_model()
def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form , 'msg' : msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_excom:
                login(request, user)
                return redirect('excom')
            elif user is not None and user.is_director:
                login(request, user)
                return redirect('director')
            elif user is not None and user.is_member:
                login(request, user)
                return redirect('member')
            else:
                msg= 'Invalid Username or Password'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

@login_required
def admin(request):
    sche = schedule.objects.all()
    params={"sche": sche}
    return render(request,'excom.html', params)

@login_required
def customer(request):
    sche = schedule.objects.all()
    params={"sche": sche}
    return render(request,'director.html', params)

@login_required
def employee(request):
    sche = schedule.objects.all()
    params={"sche": sche}
    return render(request,'member.html', params)

# def edit(request):
#     context = {}
    # check = register_table.objects.filter(user__id=request.user.id)
    # if len(check)>0:
    #     data = register_table.objects.get(user__id=request.user.id)
    #     context["data"] = data    
#     if request.method=="POST":
#         fn = request.POST["name"]
#         em = request.POST["email"]
#         con = request.POST["contact"]
#         department = request.POST["department"]

#         usr = User.objects.get(id=request.user.id)
#         usr.first_name = fn
#         usr.email = em
#         usr.save()
    
#         data.contact_number = con
#         data.department = department
#         data.save()

#         if "profile" in request.FILES:
#             img = request.FILES["profile"]
#             data.profile_pic = img
#             data.save()


#         context["status"] = "Changes Saved Successfully"
#     return render(request,"update_profile.html",context)

@login_required
def member_details(request):
    member = Members.objects.all()
    params={"member": member}
    return render (request, 'details.html', params)
@login_required
def add(request):
    context = {}
    if request.method == "POST":
        if request.POST.get('date') and request.POST.get('time') and request.POST.get('location') and request.POST.get('agenda') and request.POST.get('members') and request.POST.get('decision'):
            addi = meeting()
            addi.date = request.POST.get('date')
            addi.time = request.POST.get('time')
            addi.location = request.POST.get('location')
            addi.agenda = request.POST.get('agenda')
            addi.members = request.POST.get('members')
            addi.decision = request.POST.get('decision')
            addi.save()
            context["status"] = "Added Meeting Minutes Successfully"
            return render(request, "excom.html", context)
    return render (request, 'addMinutes.html')
@login_required
def scheduleMeeting(request):
    context ={}
    if request.method == 'POST':
        if request.POST.get('date') and request.POST.get('time') and request.POST.get('location'):
            sch = schedule()
            sch.date = request.POST.get('date')
            sch.time = request.POST.get('time')
            sch.location = request.POST.get('location')
            sch.save()
            context["status"] = "Meeting is Scheduled"
            return render(request, "scheduleMeeting.html", context)
    return render (request, 'scheduleMeeting.html')