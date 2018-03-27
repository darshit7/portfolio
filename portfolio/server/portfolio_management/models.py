from django.db import models
from django.utils.translation import ugettext_lazy as _


class Designation(models.Model):
	"""
	Model class to store designation details.
	"""
	name = models.CharField(_('Designation'), max_length=80, unique=True)

class Organization(models.Model):
	"""
	Model class to store Organization details.
	"""
	name = models.CharField(_('Name'), max_length=80, unique=True)
	designation = models.ForeignKey('Designation', verbose_name=_('Designation'),
		on_delete=models.CASCADE)
	joined_at = models.DateField(_('Joined At'))
	leaved_at = models.DateField(_('Leaved At'))

class Role(models.Model):
	"""
	Model class to store Role details.
	"""
	name = models.CharField(_('Name'), max_length=80)


class Project(models.Model):
	"""
	Model class to store project details.
	"""
	name = models.CharField(_('Name'), max_length=80)
	desc = models.TextField(_('Description'), db_column="description")
	start_from = models.DateField(_('Start From'))
	end_at = models.DateField(_('End At'), null=True, blank=True)
	organization = models.ForeignKey('Organization', verbose_name=_('Developed At'),
		on_delete=models.CASCADE)
	role = models.ManyToManyField('Role', verbose_name=_('Role'))

