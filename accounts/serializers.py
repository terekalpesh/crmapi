from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import CustomUser

class UserSerializer(RegisterSerializer, serializers.ModelSerializer):
    # email = serializers.EmailField()
    # first_name = serializers.CharField(max_length=30)
    # last_name = serializers.CharField(max_length=30)
    # full_name = serializers.CharField(max_length=60)
    # phone = serializers.CharField(max_length=10)
    # address = serializers.CharField()
    # city = serializers.CharField()
    # state = serializers.CharField()
    # country = serializers.CharField()
    # pincode = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'full_name', 'phone', 'address', 'city', 'state', 'country', 'pincode',)
        read_only_fields = ['full_name']

        def validate_first_name(self, value):
            if not value.isalpha():
                raise serializers.ValidationError("First name must contain only letters")
            return value
    
        def validate_last_name(self, value):
            if not value.isalpha():
                raise serializers.ValidationError("Last name must contain only letters")
            return value
    
        def validate_phone(self, value):
            if not value.isdigit():
                raise serializers.ValidationError("Phone number must contain only digits.")
            if len(value) < 10 or len(value) > 10:
                raise serializers.ValidationError("Phone number must be between 10 digits.")
            return value
    
        def validate_pincode(self, value):
            if not value.isdigit():
                raise serializers.ValidationError("Pincode must contain only digits.")
            if len(value) != 6:
                raise serializers.ValidationError("Pincode must be 6 digits.")
            return value
    
        def get_cleaned_data(self):
            data = super().get_cleaned_data()
            data['first_name'] = self.validated_data.get('first_name', '')
            data['last_name'] = self.validated_data.get('last_name', '')
            data['full_name'] = self.validated_data.get('full_name', '')
            data['phone'] = self.validated_data.get('phone', '')
            data['address'] = self.validated_data.get('address', '')
            data['city'] = self.validated_data.get('city', '')
            data['state'] = self.validated_data.get('state', '')
            data['country'] = self.validated_data.get('country', '')
            data['pincode'] = self.validated_data.get('pincode', '')
            return data
    
        def save(self, request):
            user = super().save(request)
            user.full_name = self.cleaned_data.get('full_name')
            user.phone = self.cleaned_data.get('phone')
            user.address = self.cleaned_data.get('address')
            user.city = self.cleaned_data.get('city')
            user.state = self.cleaned_data.get('state')
            user.country = self.cleaned_data.get('country')
            user.pincode = self.cleaned_data.get('pincode')
            user.save()
            return user