from rest_framework import serializers

from user.models import User
from prof.models import Prof


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('is_admin', 'is_active', 'last_login')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """
        'UserModel.objects.create_user(**args)' method for creating a user.

        after a user register,
        create a profile for it 
        """
        user = User.objects.create_user(**validated_data)
        prof = Prof.objects.create(user=user)
        return user
