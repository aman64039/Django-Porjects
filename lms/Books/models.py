from django.db import models

# Create your models here.


class Books(models.Model):
	book_id = models.PositiveIntegerField(unique = True)
	title = models.CharField(max_length= 200 , unique=True)
	author = models.CharField(max_length = 200 , blank = True , null = True)
	genre = models.CharField(max_length = 200 , blank = True , null = True)
	subGenre = models.CharField(max_length = 200 , blank = True , null = True)
	publisher = models.CharField(max_length = 200 , blank = True , null = True)
	count = models.PositiveIntegerField(blank = True , null = True)

	def __str__(self):
		return self.book_id