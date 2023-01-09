from django.shortcuts import render, get_object_or_404
from .models import meeting
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def meetings(request):
    meeting_minutes= meeting.objects.all()
    params={"meeting": meeting_minutes}
    return render (request, 'meeting minutes.html', params)

@login_required
def minutes(request, id):
    minutes= get_object_or_404(meeting, id=id)
    params={"meet": minutes}
    return render (request, 'minutes.html', params)

# def add(request):
#     context = {}
#     if request.method == "POST":
#          if request.POST.get('date') and request.POST.get('time') and request.POST.get('location') and request.POST.get('agenda') and request.POST.get('members') and request.POST.get('decision'):
#             addi = meeting()
#             addi.date = request.POST.get('date')
#             addi.time = request.POST.get('time')
#             addi.location = request.POST.get('location')
#             addi.agenda = request.POST.get('agenda')
#             addi.members = request.POST.get('members')
#             addi.decision = request.POST.get('decision')
#             addi.save()
#             context["status"] = "Added Meeting Minutes Successfully"
#             return render(request, "excom.html", context)



