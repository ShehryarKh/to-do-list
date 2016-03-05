from django.db import 
from django.contrib.auth.models import User


# Create your models here.

class Todo(models.Model):
	#title name
	title = models.CharField(max_length = 120)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    # Timestamp will save and set one time
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	completed = models.BooleanField()

	def __str__(self):
		return self.title
		# return "{} {}".format(self.title, self.content)


#creat a user model class
class UserProfile(models.Model):
	# link userprofile to a user model
	user = models.OneToOneField(User)

	website = models.UrlField(black=True)
	picture = models.ImageField()


