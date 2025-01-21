from django.shortcuts import render
from rest_framework import generics,permissions,viewsets
from .models import FitnessClass,Booking
from .serializers import FitnessClassSerializer,BookingSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from account.permissions import IsAuthororReadonly,IsStaff,IsMember
from account.models import CustomUser
from django.http import HttpResponseForbidden

class FitnessClassView(generics.ListAPIView):
    queryset=FitnessClass.objects.all()
    serializer_class=FitnessClassSerializer

class FitnessClassCreate(generics.CreateAPIView):
    queryset=FitnessClass.objects.all()
    serializer_class=FitnessClassSerializer
    permission_classes=[IsStaff]

class FitnessClassDetailView(generics.RetrieveAPIView):
    queryset=FitnessClass.objects.all()
    serializer_class=FitnessClassSerializer
    
class FitnessClassUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=FitnessClass.objects.all()
    serializer_class=FitnessClassSerializer
    permission_classes=[IsStaff]

class BookingView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes=[IsMember]

    def perform_create(self, serializer):
        serializer.save(member=self.request.user)

class BookingHistory(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsMember]
    

    def get_queryset(self):
        if not self.request.user.is_authenticated:
         return HttpResponseForbidden("You must be logged in to access this page.")
        user=self.request.user
        return Booking.objects.filter(member=user)
    
    
class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
   
    queryset =Booking.objects.all()
    serializer_class = BookingSerializer
   
    permission_classes=[IsAuthororReadonly]

    
    def get_queryset(self):
        user=self.request.user
        return Booking.objects.filter(member=user)

   