from django.shortcuts import render
from rest_framework.views import APIView
from . import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics,permissions
from .models import CustomUser,MemberProfile,GymPlan
from .serializers import UserSerializer,PlanSerializer,ProfileSerializer,UserLoginSerializer,MemDelSerializer
from .permissions import IsStaff,IsAuthororReadonly,IsMember,IsOwner
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,AllowAny
# for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect

class UserRegistrationApiView(APIView):
    serializer_class = serializers.UserSerializer
    permission_classes=[AllowAny]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            print("token ", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid ", uid)
            confirm_link = f"https://gym-manage-delta.vercel.app/active/{uid}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            
            email = EmailMultiAlternatives(email_subject , '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Check your mail for confirmation")
        return Response(serializer.errors)


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = CustomUser._default_manager.get(pk=uid)
    except(CustomUser.DoesNotExist):
        user = None 
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')
    
class UserLoginApiView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data = self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username= username, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request, user)
                return Response({'token' : token.key, 'user_id' : user.id})
            else:
                return Response({'error' : "Invalid Credential"})
        return Response(serializer.errors)

class UserLogutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')   

class MemberListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(user_type='member')
    serializer_class = MemDelSerializer
    permission_classes=[IsStaff]



class MemberDeleteView(generics.RetrieveDestroyAPIView):
    queryset = CustomUser.objects.filter(user_type='member')
    serializer_class = MemDelSerializer
    permission_classes=[IsStaff]


class MemberProfleView(viewsets.ModelViewSet):
    queryset =MemberProfile.objects.all()
    serializer_class =ProfileSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        qs=super().get_queryset()

        return qs.filter(user=self.request.user)
    

class PlanList(generics.ListAPIView):
    queryset=GymPlan.objects.all()
    serializer_class=PlanSerializer

class PlanCreate(generics.CreateAPIView):
    queryset=GymPlan.objects.all()
    serializer_class=PlanSerializer
    permission_classes=[IsStaff]

class PlanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=GymPlan.objects.all()
    serializer_class=PlanSerializer
    permission_classes=[IsStaff]
    





