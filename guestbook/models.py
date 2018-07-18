from django.db import models

# Create your models here.

class Guestbook(models.Model):
    name = models.CharField(max_length=12)
    password = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "User(%s, %s, %s)" % (self.name, self.content, self.datetime)