from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from portfolio_management.models import Role, Designation, Organization, \
        Project

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name',)

    def create(self, validated_data):
        '''
        '''
        return Role.objects.create(name=validated_data.get('name'))

    def update(self, instance, validated_data):
        '''
        '''
        instance.role = validated_data.get('name', instance.name)
        instance.save()
        return instance

class DesignationSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Designation
        fields = ('id', 'name')

    def create(self, validated_data):
        """
        """
        return Designation.objects.create(name=validated_data.get('name'))

    def update(self, instance, validated_data):
        """
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class OrganizationSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Organization
        fields = ('id', 'name', 'designation', 'joined_at', 'leaved_at')

    def create(self, validated_data):
        """
        """
        return Organization.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.designation = validated_data.get('designation',
            instance.designation)
        instance.joined_at = validated_data.get('joined_at',
            instance.joined_at)
        instance.leaved_at = validated_data.get('leaved_at',
            instance.leaved_at)
        return instance

class ProjectSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Project
        fields = ('id', 'name', 'desc', 'start_from', 'end_at', 'organization',
            'role')

    def create(self, validated_data):
        """
        """
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        """
        instance.name = validated_data.get('name', instance.name)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.start_from = validated_data.get('start_from',
            instance.start_from)
        instance.end_at = validated_data.get('end_at', instance.end_at)
        instance.organization = validated_data.get('organization',
            instance.organization)
        instance.role = validated_data.get('role', instance.role)
