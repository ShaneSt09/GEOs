from django.contrib import admin
from .models import Community
from .models import CommunityType
from .models import Parish

admin.site.register(Community)
admin.site.register(CommunityType)
admin.site.register(Parish)