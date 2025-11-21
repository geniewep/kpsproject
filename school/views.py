from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm as UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

# Simple views that render the static templates located in school/templates/
# Each view returns the appropriate template. These are intentionally
# lightweight so you can later add authentication/permissions or context.

def admin_dashboard_light(request):
	return render(request, 'admin_dashboardl.html')


def admin_dashboard_dark(request):
	return redirect('admin_dashboard_light')


def attendance_teachers_light(request):
	return render(request, 'attendace_taking_screen_for_teacherslight.html')
 

def attendance_teachers_dark(request):
	return redirect('attendance_teachers_light')


def grading_marks_entry_light(request):
	return render(request, 'grading_marks_entrylight.html')


def grading_marks_entry_dark(request):
	return redirect('grading_marks_entry_light')


def messaging_interface_light(request):
	return render(request, 'messaging_interface_light.html')


def messaging_interface_dark(request):
	return redirect('messaging_interface_light')


@login_required(login_url='login')
def parent_dashboard_light(request):
	return render(request, 'parent_dashboardlight.html')


@login_required(login_url='login')
def parent_dashboard_dark(request):
	return redirect('parent_dashboard_light')


def report_generation_for_admin(request):
	return render(request, 'report_generation_for_admin.html')


def school_wide_announcements(request):
	return render(request, 'school_wide_announcements.html')


def student_profile_light(request):
	return render(request, 'student_profile_light.html')


def student_profile_dark(request):
	return redirect('student_profile_light')


@login_required(login_url='login')
def teacher_dashboard_light(request):
	# Ensure only users with the teacher role can access this dashboard.
	user_role = getattr(request.user, 'role', None)
	if user_role != 'teacher':
		messages.error(request, 'You do not have permission to access the teacher dashboard.')
		# Redirect to the appropriate dashboard for their role
		if user_role == 'parent':
			return redirect('parent_dashboard_light')
		else:
			return redirect('admin_dashboard_light')

	return render(request, 'teacher_dashboard_for_school_management_system_light.html')


def teacher_dashboard_dark(request):
	return redirect('teacher_dashboard_light')


def user_management(request):
	"""Render the user management screen for admins.

	This view serves the template `user_management_screen_for_admin.html`.
	"""
	return render(request, 'user_management_screen_for_admin.html')


def system_settings(request):
	"""Simple placeholder for system settings. Renders the reports template for now."""
	return render(request, 'report_generation_for_admin.html')


def calendar(request):
	"""Simple placeholder for calendar view. Renders the reports template for now."""
	# Render the dedicated calendar template
	# Provide a simple days sequence for the template to iterate over
	days = range(1, 31)
	return render(request, 'calendar.html', {'days': days})


def login_view(request):
	"""Render login form and authenticate users using Django's AuthenticationForm.

	On success the user is logged in and redirected to the admin dashboard.
	"""
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			auth_login(request, user)
			# Prefer the authenticated user's role (safer than trusting POST). Fall back to POST for older flows.
			role = getattr(user, 'role', None) or request.POST.get('role')
			if role:
				request.session['role'] = role
			# Redirect based on the user's actual role (fallback to admin dashboard)
			if role == 'parent':
				return redirect('parent_dashboard_light')
			elif role == 'teacher':
				return redirect('teacher_dashboard_light')
			else:
				return redirect('admin_dashboard_light')
		else:
			messages.error(request, 'Login failed. Please check your credentials and try again.')
	else:
		form = AuthenticationForm()

	return render(request, 'auth/login.html', {'form': form})


def register_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			# capture chosen role from the registration form and store in session
			role = request.POST.get('role')
			if role:
				request.session['role'] = role
			# Save optional email and role on the user object if provided
			email = request.POST.get('email')
			if email:
				user.email = email
			if role:
				# assign the role field on the custom user model (avoid leaving it empty)
				user.role = role
			user.save()
			# Try to authenticate; some environments with a swapped user model
			# can raise manager access errors when calling authenticate().
			# To avoid that, attempt authenticate() but fall back to setting
			# the backend on the user object and logging them in directly.
			raw_password = form.cleaned_data.get('password1')
			user_auth = None
			try:
				user_auth = authenticate(request, username=user.username, password=raw_password)
			except Exception:
				user_auth = None
			if user_auth is not None:
				auth_login(request, user_auth)
				messages.success(request, 'Registration successful. You are now logged in.')
			else:
				# If authenticate() fails (or throws due to swapped model manager),
				# set the backend attribute on the user instance and log them in.
				user.backend = 'django.contrib.auth.backends.ModelBackend'
				auth_login(request, user)
				messages.success(request, 'Registration successful. You are now logged in.')
			# Redirect based on selected role
			# prefer role stored on the user instance (in case form POST didn't include it)
			role = getattr(user, 'role', None) or role
			if role == 'parent':
				return redirect('parent_dashboard_light')
			elif role == 'teacher':
				return redirect('teacher_dashboard_light')
			else:
				return redirect('admin_dashboard_light')
		else:
			messages.error(request, 'Please correct the errors below.')
	else:
		form = UserCreationForm()

	return render(request, 'auth/registration.html', {'form': form})


def forgot_password(request):
	"""Render the forgot-password template. Implementing actual reset flows is a separate task.

	This placeholder simply renders the template located at `templates/auth/forgot password.html`.
	"""
	return render(request, 'auth/forgot password.html')


def logout_view(request):
	"""Log out the current user and redirect to the login page."""
	auth_logout(request)
	# clear any role stored in session
	if 'role' in request.session:
		request.session.pop('role')
	return redirect('login')

