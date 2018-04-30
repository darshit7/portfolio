import json

from django.http import Http404

from rest_framework import status, views, permissions
from rest_framework.response import Response

from portfolio_management.serializers import (RoleSerializer,
	DesignationSerializer, OrganizationSerializer, ProjectSerializer)
from portfolio_management.models import (Role, Designation, Organization,
        Project)

class RoleView(views.APIView):
	"""
	"""
	def get_object(self, pk):
		try:
			return Role.objects.get(pk=pk)
		except Role.DoesNotExist:
			raise Http404

	def get(self, request, pk=None, format=None):
		"""
		"""
		if not pk:
			serializer = RoleSerializer(Role.objects.all(), many=True)
			return Response(serializer.data)
		else:
			serializer = RoleSerializer(self.get_object(pk))
			return Response(serializer.data)

	def put(self, request, pk, format=None):
		"""
		"""
		role = self.get_object(pk)
		serializer = RoleSerializer(role, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		"""
		"""
		role = self.get_object(pk)
		role.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	def post(self, request, format=None):
		"""
		"""
		serializer = RoleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DesignationView(views.APIView):
	"""
	"""
	def get_object(self, pk):
		try:
			return Designation.objects.get(pk=pk)
		except Designation.DoesNotExist:
			raise Http404

	def get(self, request, pk=None, format=None):
		"""
		"""
		if not pk:
			serializer = DesignationSerializer(Designation.objects.all(), many=True)
			return Response(serializer.data)
		else:
			serializer = DesignationSerializer(self.get_object(pk))
			return Response(serializer.data)

	def put(self, request, pk, format=None):
		"""
		"""
		designation = self.get_object(pk)
		serializer = DesignationSerializer(designation, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		"""
		"""
		designation = self.get_object(pk)
		designation.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	def post(self, request, format=None):
		"""
		"""
		serializer = DesignationSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrganizationView(views.APIView):
	"""
	"""
	def get_object(self, pk):
		try:
			return Organization.objects.get(pk=pk)
		except Organization.DoesNotExist:
			raise Http404

	def get(self, request, pk=None, format=None):
		"""
		"""
		if not pk:
			serializer = OrganizationSerializer(Organization.objects.all(), many=True)
			return Response(serializer.data)
		else:
			serializer = OrganizationSerializer(self.get_object(pk))
			return Response(serializer.data)

	def put(self, request, pk, format=None):
		"""
		"""
		organization = self.get_object(pk)
		serializer = RoleSerializer(organization, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		"""
		"""
		organization = self.get_object(pk)
		organization.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	def post(self, request, format=None):
		"""
		"""
		serializer = OrganizationSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectView(views.APIView):
	"""
	"""
	def get_object(self, pk):
		try:
			return Project.objects.get(pk=pk)
		except Project.DoesNotExist:
			raise Http404

	def get(self, request, pk=None, format=None):
		"""
		"""
		if not pk:
			serializer = ProjectSerializer(Project.objects.all(), many=True)
			return Response(serializer.data)
		else:
			serializer = ProjectSerializer(self.get_object(pk))
			return Response(serializer.data)

	def put(self, request, pk, format=None):
		"""
		"""
		project = self.get_object(pk)
		serializer = ProjectSerializer(role, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		"""
		"""
		project = self.get_object(pk)
		project.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	def post(self, request, format=None):
		"""
		"""
		serializer = ProjectSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
