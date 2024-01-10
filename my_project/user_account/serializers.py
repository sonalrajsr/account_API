from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password_2 = serializers.CharField(write_only = True)

    class Meta:
        mod
        el = User
        fields = ['username', 'email', 'password', 'password_2']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }
    
    def save(self):
        password = self.validated_data['password']
        password_2 = self.validated_data['password_2']

        if password != password_2:
            raise serializers.ValidationError('Password must be same')
        
        if User.objects.filter(email = self.validated_data['email']).exists():
            raise serializers.ValidationError('Email already exists')
        
        account = User(email = self.validated_data['email'], username = self.validated_data['username'])
        account.set_password(password)
        account.save()
        
        return account