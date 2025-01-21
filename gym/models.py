from django.db import models
from account.models import CustomUser
# Create your models here.

class FitnessClass(models.Model):
    name=models.CharField(max_length=100)
    instructor=models.CharField(max_length=50)
    schedule=models.DateTimeField()
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    member=models.ForeignKey(CustomUser,on_delete=models.CASCADE,limit_choices_to={'user_type': 'member'},related_name='book')
    fitness_class=models.ForeignKey(FitnessClass,on_delete=models.CASCADE,related_name='cls')
    booking_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.username} - {self.fitness_class.name}"