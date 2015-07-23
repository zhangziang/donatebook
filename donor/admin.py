from django.contrib import admin

from .models import Donor

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'college')
    search_fields = ('name',)
