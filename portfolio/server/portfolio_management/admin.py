from django.contrib import admin

from portfolio_management.models import Designation, Organization, \
    Role, Project

class DesignationAdmin(admin.ModelAdmin):
	pass

class OrganizationAdmin(admin.ModelAdmin):
	pass

class RoleAdmin(admin.ModelAdmin):
	pass

class ProjectAdmin(admin.ModelAdmin):
	pass

admin.site.register(Designation, DesignationAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Project, ProjectAdmin)
