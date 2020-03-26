from django.contrib import admin
from .models import MainCategory,ArticleSeries,MainArticle
from tinymce.widgets import TinyMCE
from django.db import models


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	fieldsets = [
		("Title/date", {"fields": ["article_title", "date_published"]}),
		("URL", {"fields":["article_slug"]}),
		("Series", {"fields":["article_series"]}),
		("Content", {"fields":["article_content"]})
	]

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}


admin.site.register(ArticleSeries)
admin.site.register(MainCategory)

admin.site.register(MainArticle, ArticleAdmin)

