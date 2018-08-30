from django.db import models

class Car(models.Model):
	production_year = models.IntegerField()
	mileage_start= models.IntegerField()
	mileage_end = models.IntegerField()
	plate_number = models.CharField(max_length=10)
	color = models.CharField(max_length=20)
	location_id = models.CharField(max_length=50)
	status = models.BooleanField(default=True)
	brand = models.CharField(max_length=15)
	models = models.CharField(max_length=10)



