from django.contrib import admin

from leads.models import Agent, Lead, User

admin.site.register(Agent)
admin.site.register(Lead)
admin.site.register(User)
