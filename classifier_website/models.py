from django.conf import settings
from django.db import models


class Post(models.Model):
	url = models.TextField()
