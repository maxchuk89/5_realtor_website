from django.contrib import admin
from .models import Flat, Complaint, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ("town", "address", "owned_by__name")
    readonly_fields = ("created_at",)
    list_display = ("address", "price", "new_building", "construction_year", "town")
    list_editable = ("new_building",)
    list_filter = ("new_building",)
    raw_id_fields = ("likes",)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ("user", "flat")


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("owned_flats",)
