from django.contrib import admin
from .models import meeting, schedule

# Register your models here.
admin.site.register(meeting)

class Schedule_Meeting(admin.ModelAdmin):
    list_display= ('id','date', 'time', 'location')
admin.site.register(schedule, Schedule_Meeting)