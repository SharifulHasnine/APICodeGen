from django.db import models
from django.conf import settings

# Create your models here.
class SampleCode(models.Model):
	id = models.AutoField(primary_key=True,)
	code = models.IntegerField(null=False)
	status = models.IntegerField(null=False,default=0)
	class Meta:
		managed = True
		db_table = 'Sample_code'

