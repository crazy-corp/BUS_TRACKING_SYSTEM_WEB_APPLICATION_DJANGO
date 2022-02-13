from django.db import models
from django.contrib.postgres.fields import ArrayField
#from django_mysql.models import ListCharField
#from jsonfield import JSONField
from django.db.models import JSONField
# Create your models here.

class sfed(models.Model):
	BusName = models.CharField(max_length=100)
	Bus_ID = models.IntegerField(primary_key=True)
	Sce = JSONField(default=dict, blank=True)
	curr_s = models.CharField(max_length=100,default="NOT AVAILABLE")
	days=models.CharField(max_length=100,default="SU MO TU WE TH FR SA")