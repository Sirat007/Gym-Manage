from rest_framework import serializers
from .models import CustomUser,MemberProfile,GymPlan,PlanAdd
from gym.models import Booking
class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only = True)
    class Meta:
        model=CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password','user_type']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        user_type = self.validated_data['user_type']
        
        if password != password2:
            raise serializers.ValidationError({'error' : "Password Doesn't Mactched"})
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email Already exists"})
        account =CustomUser(username = username, email=email, first_name = first_name, last_name = last_name,user_type=user_type)
        print(account)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')  
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            user_type=validated_data['user_type']
        )
        return user
userchoice=(
        ('member','Member'),
        ('staff','Staff'),
    )

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
    user_type=serializers.ChoiceField(choices=userchoice)

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model=GymPlan
        fields='__all__'

    
class MemDelSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        exclude=['password']        

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['id','first_name', 'last_name', 'email','user_type']
          
class MemberPlan(serializers.ModelSerializer):
    class Meta:
        model=GymPlan
        fields='__all__'

class ProfileSerializer(serializers.ModelSerializer):
    user=MemberSerializer(read_only=True)
    class Meta:
        model = MemberProfile
        fields = '__all__'

    def create(self, validated_data):
        
        return MemberProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        
       
        instance.plan = validated_data.get('plan', instance.plan)
        instance.save()
        return instance

class PlanAddSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlanAdd
        fields='__all__'
