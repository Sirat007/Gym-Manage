from django.contrib import admin
from . models import CustomUser,MemberProfile,GymPlan
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(MemberProfile)
admin.site.register(GymPlan)
admin.site.register(PlanAdd)
