from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'date_of_birth',)


class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)  #not to include it in the output
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'date_of_birth',)
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        print("Validating input data:", attrs)
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError("Passwords do not match")

        password = attrs.get('password1')
        if len(password) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters")

        for field_name in ['first_name', 'last_name', 'date_of_birth', 'email', 'password1', 'password2']:
            if field_name not in attrs:
                if field_name == 'password1':
                    raise serializers.ValidationError("Password field is required")
                elif field_name == 'password2':
                    raise serializers.ValidationError("Confirm Password field is required")
                else:
                    raise serializers.ValidationError("{} field is required".format(field_name))
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password1')
        validated_data.pop('password2')
        email = validated_data.pop('email')
        user = User.objects.create_user(email=email, password=password, **validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials")


