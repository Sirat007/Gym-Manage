from django.urls import path,include
from .views import UserRegistrationApiView,UserLoginApiView,UserLogutView,MemberListView,MemberProfleView,MemberDeleteView,activate,PlanCreate,PlanList,PlanDetail,UserDetail
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'profile',MemberProfleView, basename='profile')
#router.register(r'detail',UserDetail,basename='detail')
urlpatterns = [
    path('register/',UserRegistrationApiView.as_view(), name='register'),
    path('login/',UserLoginApiView.as_view(), name='login'),
    path('logout/',UserLogutView.as_view(), name='logout'),
    path('active/<uid64>/<token>/',views.activate, name = 'activate'),
    path('members/',MemberListView.as_view(),name='memberlist'),
    path('members/<int:pk>',MemberDeleteView.as_view(),name='deletemember'),
    #path('profile/',MemberProfleView.as_view(),name='profile'),
    #path('profile/<int:pk>',ProfileDetailView.as_view(),name='profiledetail'),
    path('planlist/',PlanList.as_view(),name='plan'),
    path('plancreate/',PlanCreate.as_view(),name='plancreate'),
    path('planedit/<int:pk>',PlanDetail.as_view(),name='planedit'),
    path('',include(router.urls)),
]


