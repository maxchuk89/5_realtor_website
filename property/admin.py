from django.contrib import admin
from .models import Flat, Owner, Complaint


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner',)
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'town', 'active', 'new_building')
    list_editable = ('active', 'new_building')
    raw_id_fields = ('liked_by',) 


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('full_name', 'phone_number', 'pure_phone')
    list_display = ('full_name', 'phone_number', 'pure_phone')
    raw_id_fields = ('flats',) 


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('complainant', 'flat', 'text')
    raw_id_fields = ('complainant', 'flat') 
