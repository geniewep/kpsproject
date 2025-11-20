
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # include the school app at the site root (no leading slash)
    path('', include('school.urls')),
]
