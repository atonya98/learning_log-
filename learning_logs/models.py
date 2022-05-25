from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
	'''specific Topic added '''
	text = models.CharField(max_length = 200)
	date_added = models.DateTimeField(auto_now_add = True)
	owner = models.ForeignKey(User,on_delete=models.CASCADE)


	def __str__(self):
		return self.text


class Entry(models.Model):
	'''Something specific learned about a topic  '''
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)

	class meta():
		verbose_name_plural = 'entries'

	def __str__(self):
		'''return a string rep of the text for the first 50 characters '''
		return self.text[:50]+'...'



