from rest_framework import serializers
from . models import FitnessClass,Booking

class FitnessClassSerializer(serializers.ModelSerializer):
    class Meta:
        model=FitnessClass
        fields='__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields='__all__'
        extra_kwargs = {
            'member': {'read_only': True}
        }

   

        

