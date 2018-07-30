from django.db import models
import datetime

# Create your models here.
class Diagnosis(models.Model):
	name = models.CharField(max_length = 100, default = "NULL")
	date = models.CharField(max_length = 100, default = "NULL")