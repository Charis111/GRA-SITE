from django.contrib import admin
from django.db import models
from .models import legals_pannel,publications_pannel,contacts_pannel,locations_pannel
from tinymce.widgets import TinyMCE

# Register your models here.



class others_Admin(admin.ModelAdmin):
	fieldsets = [
		("Title", {"fields": ["title"]}),
		("Content", {"fields":["content"]}),
		("thumb", {"fields":["thumb"]})
	]

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}

admin.site.register(legals_pannel,others_Admin)
admin.site.register(publications_pannel,others_Admin)
admin.site.register(contacts_pannel,others_Admin)
admin.site.register(locations_pannel,others_Admin)