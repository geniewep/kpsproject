from django.urls import path
from . import views

urlpatterns = [
	# Avoid using the "admin/" prefix so these views are not confused with Django's admin site
	# Landing page should be the login page
	path('', views.login_view, name='login'),
	# Admin dashboard (light and dark variants)
	path('admin-dashboard/light/', views.admin_dashboard_light, name='admin_dashboard_light'),
	path('admin-dashboard/dark/', views.admin_dashboard_dark, name='admin_dashboard_dark'),

	path('attendance/teachers/light/', views.attendance_teachers_light, name='attendance_teachers_light'),
	path('attendance/teachers/dark/', views.attendance_teachers_dark, name='attendance_teachers_dark'),

	path('grading/marks/light/', views.grading_marks_entry_light, name='grading_marks_entry_light'),
	path('grading/marks/dark/', views.grading_marks_entry_dark, name='grading_marks_entry_dark'),

	path('messaging/light/', views.messaging_interface_light, name='messaging_interface_light'),
	path('messaging/dark/', views.messaging_interface_dark, name='messaging_interface_dark'),

	path('parent/dashboard/light/', views.parent_dashboard_light, name='parent_dashboard_light'),
	path('parent/dashboard/dark/', views.parent_dashboard_dark, name='parent_dashboard_dark'),

	path('reports/generate/', views.report_generation_for_admin, name='report_generation_for_admin'),
	path('announcements/', views.school_wide_announcements, name='school_wide_announcements'),

	path('student/profile/light/', views.student_profile_light, name='student_profile_light'),
	path('student/profile/dark/', views.student_profile_dark, name='student_profile_dark'),

	path('teacher/dashboard/light/', views.teacher_dashboard_light, name='teacher_dashboard_light'),
	path('teacher/dashboard/dark/', views.teacher_dashboard_dark, name='teacher_dashboard_dark'),
	# User management
	path('user-management/', views.user_management, name='user_management'),
	path('settings/', views.system_settings, name='system_settings'),
	path('calendar/', views.calendar, name='calendar'),

	# Authentication (login / register / password)
	# Keep a dedicated login URL as well, but avoid duplicating the 'login' name
	path('auth/login/', views.login_view, name='login_page'),
	path('auth/register/', views.register_view, name='register'),
	path('auth/forgot-password/', views.forgot_password, name='forgot_password'),
	path('auth/logout/', views.logout_view, name='logout'),
]
