from django.shortcuts import render

# Simple views that render the static templates located in school/templates/
# Each view returns the appropriate template. These are intentionally
# lightweight so you can later add authentication/permissions or context.

def admin_dashboard_light(request):
	return render(request, 'admin_dashboardl.html')


def admin_dashboard_dark(request):
	return render(request, 'admin_dashboarddark.html')


def attendance_teachers_light(request):
	return render(request, 'attendace_taking_screen_for_teacherslight.html')


def attendance_teachers_dark(request):
	return render(request, 'attendace_taking_screen_for_teachersdark.html')


def grading_marks_entry_light(request):
	return render(request, 'grading_marks_entrylight.html')


def grading_marks_entry_dark(request):
	return render(request, 'grading_marks_entrydark.html')


def messaging_interface_light(request):
	return render(request, 'messaging_interface_light.html')


def messaging_interface_dark(request):
	return render(request, 'messaging_interfacedark.html')


def parent_dashboard_light(request):
	return render(request, 'parent_dashboardlight.html')


def parent_dashboard_dark(request):
	return render(request, 'parent_dashboarddark.html')


def report_generation_for_admin(request):
	return render(request, 'report_generation_for_admin.html')


def school_wide_announcements(request):
	return render(request, 'school_wide_announcements.html')


def student_profile_light(request):
	return render(request, 'student_profile_light.html')


def student_profile_dark(request):
	return render(request, 'student_profiledark.html')


def teacher_dashboard_light(request):
	return render(request, 'teacher_dashboard_for_school_management_system_light.html')


def teacher_dashboard_dark(request):
	return render(request, 'teacher_dashboard_for_school_management_system_dark.html')

