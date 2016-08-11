from django.contrib import admin

# Register your models here.
from .models import mysite

class mysiteadmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name']}),
		('Date info', {'fields': ['due_date'], 'classes': ['collapse']})
	
	]
	
admin.site.register(mysite,mysiteadmin)	