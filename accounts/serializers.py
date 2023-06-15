from rest_framework import serializers
from accounts.models import User
from django.contrib import auth
from rest_framework import exceptions

class RegisterSerializer(serializers.ModelSerializer):
    '''
    Registration Serializer
    '''

    class Meta:
        model = User
        fields = (
            'id', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    '''
    Login serializer
    '''
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=255)
    first_name = serializers.CharField(max_length=255, read_only=True)
    last_name = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(min_length=1, write_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, instance):
        '''
        returns the object returned by tokens method in AUTH_USER_MODEL
        '''

        user = User.objects.get(email=instance['email'])
        
        return {
            "refresh_token": user.tokens()['refresh_token'],
            "access_token": user.tokens()["access_token"]
        }
    
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'tokens')

    
    def validate(self, attrs):
        '''
        validate method - validates the instance passed to the serializer
        '''

        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise exceptions.AuthenticationFailed('Invalid credentials, try again')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('Account Disabled, contact admin')

        return {
            "id":user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "tokens": user.tokens
        }


        

