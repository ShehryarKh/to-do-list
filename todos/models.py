from django.db import models

# Create your models here.


class Todo(models.Model):
	#title name
	title = models.CharField(max_length = 120)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    # Timestamp will save and set one time
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	completed = models.BooleanField(default=True)

	def __str__(self):
		return self.title
		# return "{} {}".format(self.title, self.content)
