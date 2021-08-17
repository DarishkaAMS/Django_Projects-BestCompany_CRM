from django.contrib import admin

from leads.models import User, Lead

admin.site.register(User)
admin.site.register(Lead)
