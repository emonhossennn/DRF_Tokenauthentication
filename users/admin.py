

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib import admin  # <-- THIS LINE IS ESSENTIAL
from .models import Job, Application  
from jobs.models import Job  
# Correct
from jobs.models import Job  # Correct way to import Job from the jobs app






# Register models with the admin panel
admin.site.register(Job)
admin.site.register(Application)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
