from django.contrib import admin
from .models import Community
from .models import CommunityType
from .models import Parish

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ('parish',)
    list_display = ('type',)

@admin.register(CommunityType)
class CommunityTypeAdmin(admin.ModelAdmin):
    ordering = ['name']

@admin.register(Parish)
class ParishAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ('code',)