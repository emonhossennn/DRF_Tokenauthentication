
from django.contrib import admin
from .models import Job, Application  
from django.contrib import admin  # This line is necessary
from .models import Job, Application  # Import your models here

# Register your models here
admin.site.register(Job)
admin.site.register(Application)



