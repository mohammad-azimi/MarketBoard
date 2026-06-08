from django.contrib import admin

from .models import Category, Favorite, Item


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "Category",
        "price",
        "condition",
        "location",
        "is_sold",
        "created_by",
        "created_at",
    )
    list_filter = (
        "Category",
        "condition",
        "is_sold",
        "created_at",
    )
    search_fields = (
        "name",
        "description",
        "location",
        "created_by__username",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "item",
        "created_at",
    )
    list_filter = (
        "created_at",
    )
    search_fields = (
        "user__username",
        "item__name",
    )
    readonly_fields = (
        "created_at",
    )