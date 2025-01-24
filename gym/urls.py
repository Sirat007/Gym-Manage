from django.urls import path
from .views import FitnessClassView,BookingView,FitnessClassDetailView,BookingDetailView,FitnessClassCreate,FitnessClassUpdate,BookingHistory
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

urlpatterns = [
    path('list',FitnessClassView.as_view(),name="fitnessclass"),
    path('create/',FitnessClassCreate.as_view(),name='create'),
    path('list/<int:pk>',FitnessClassDetailView.as_view(),name='classdetail'),
    path('delete/<int:pk>',FitnessClassUpdate.as_view(),name='deletecls'),
    #path('booking/',BookingView.as_view(),name="booking"),
    path('bookinglist/',BookingHistory.as_view(),name='bookinghistory'),
    path('booking/<int:pk>',BookingDetailView.as_view(),name='bookingdetail'),
]

router.register(r'booking',BookingView, basename='booking')

urlpatterns += router.urls
