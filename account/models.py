from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

#from gym.models import Booking
# Create your models here.
class CustomUser(AbstractUser):
    User_Type_Choices=(
        ('member','Member'),
        ('staff','Staff'),
    )

    user_type=models.CharField(max_length=10, choices=User_Type_Choices,default="member")
    

@receiver(post_save, sender=CustomUser)
def create_member_profile(sender, instance, created, **kwargs):
    if created:
        MemberProfile.objects.create(user=instance)

Plan_Choices=[
    ('weekly','weekly'),
    ('monthly','monthly'),
    ('yearly','yearly'),
]

class GymPlan(models.Model):
    name=models.CharField(max_length=20,choices=Plan_Choices)
    price=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name
    



class MemberProfile(models.Model):
    user=models.OneToOneField(CustomUser,null=True,blank=True,on_delete=models.CASCADE,related_name="profile")
    
    plan=models.ForeignKey(GymPlan,null=True,blank=True,on_delete=models.SET_NULL,related_name='plan')
    bio=models.CharField(max_length=50,null=True,blank=True)

class PlanAdd(models.Model):                                                                                                                    
    user=models.OneToOneField(CustomUser,null=True,blank=True,on_delete=models.CASCADE,related_name="add")
    booking_date=models.DateTimeField(auto_now_add=True)
    plan=models.ForeignKey(GymPlan,on_delete=models.SET_NULL,null=True,blank=True,related_name='plans')
    def __str__(self):
        return f"{self.user.username} - {self.plan.name}"
