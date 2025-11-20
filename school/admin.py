from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(AcademicYear)
admin.site.register(Term)
admin.site.register(SchoolClass)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Assessment)
admin.site.register(GradeEntry)
admin.site.register(AttendanceRecord)
admin.site.register(BehaviourIncident)
admin.site.register(MessageThread)
admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(TermReport)