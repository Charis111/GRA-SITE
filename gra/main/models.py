from django.db import models
from datetime import datetime

# Create your models here.

class MainCategory(models.Model):
	"""docstring for MianCategory"""

	main_category=models.CharField(max_length=200)
	cat_summary = models.CharField(max_length=200)
	cat_slug = models.CharField(max_length=200)
	image=models.ImageField( default = 'img/img.jpg')

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.main_category





class ArticleSeries(models.Model):
	article_series = models.CharField(max_length=200)
	main_category = models.ForeignKey(MainCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
	series_summary = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Series"

	def __str__(self):
		return self.article_series





class MainArticle(models.Model):
	article_title = models.CharField(max_length=200)
	article_content = models.TextField()
	date_published = models.DateTimeField("date published", default=datetime.now())

	article_series = models.ForeignKey(ArticleSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
	article_slug = models.CharField(max_length=200, default=1)
	thumb = models.ImageField(default='default.png', blank=True)

	def __str__(self):
		return self.article_title


	# def snippet(self):
 #        return self.body[:50] + '...'




        

