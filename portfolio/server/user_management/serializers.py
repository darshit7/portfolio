'''
'''

from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from user_management.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'full_name', 'email', 'created_at', 'password',
                'confirm_password', 'is_admin', 'is_staff',
                'is_active', 'is_deleted')
        read_only_fields = ('created_at', )

    def create(self, validated_data):
        '''
        '''
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        '''
        '''
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)
        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()
        update_session_auth_hash(self.context.get('request'), instance)
        return instance
