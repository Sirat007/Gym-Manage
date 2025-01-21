from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    User_Type_Choices=(
        ('member','Member'),
        ('staff','Staff'),
    )

    user_type=models.CharField(max_length=10, choices=User_Type_Choices,default="member")

Plan_Choices=[
    ('weekly','weekly'),
    ('monthly','monthly'),
    ('yearly','yearly'),
]

class GymPlan(models.Model):
    name=models.CharField(max_length=20,choices=Plan_Choices)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name

class MemberProfile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="profile")
    plan=models.ForeignKey(GymPlan,null=True,blank=True,on_delete=models.SET_NULL,related_name='plan')

    def __str__(self):
        return self.user.username