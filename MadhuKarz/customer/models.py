from django.contrib.auth.models import AbstractUser
from django.db import models
from car.models import Car


class CustomUser(AbstractUser):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	license_number = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=10)

	def __str__(self):
		return self.email


#If you use the default authentication backend, then your model must have a single unique field 
#that can be used for identification purposes. This can be a username, an email address, or any

class reservation(models.Model):
	customer_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE, verbose_name='related customer_id')
	car_id = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='related car_id')
	pick_location_id = models.CharField(max_length=50)
	dropoff_location_id = models.CharField(max_length=20)
	start_date = models.DateField()
	end_date = models.DateField()
	remarks = models.CharField(max_length=300)
	fuel_option_id = models.IntegerField()
	rental_insurance_id = models.IntegerField()


class Rental_Invoice(models.Model):
	rental_id = models.ForeignKey(reservation, on_delete=models.CASCADE, verbose_name='related rental_id')
	car_rent = models.FloatField()
	insurance_cost = models.FloatField()
	GST = models.FloatField()
	total_amount_payable = models.FloatField()




