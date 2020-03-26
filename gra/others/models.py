from django.db import models

# Create your models here.
class legals_pannel(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	thumb = models.ImageField(default='default.png')

	def __str__(self):
		return self.title




class publications_pannel(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	thumb = models.ImageField(default='default.png')

	def __str__(self):
		return self.title





class contacts_pannel(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	thumb = models.ImageField(default='default.png')

	def __str__(self):
		return self.title




class locations_pannel(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	thumb = models.ImageField(default='default.png')

	def __str__(self):
		return self.title

