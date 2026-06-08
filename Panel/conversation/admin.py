from django.contrib import admin

from .models import Conversation, ConversationMessage


class ConversationMessageInline(admin.TabularInline):
    model = ConversationMessage
    extra = 0
    readonly_fields = ("created_at",)
    filter_horizontal = ("read_by",)


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = (
        "item",
        "created_at",
        "modified_at",
    )
    list_filter = (
        "created_at",
        "modified_at",
    )
    search_fields = (
        "item__name",
        "members__username",
    )
    readonly_fields = (
        "created_at",
        "modified_at",
    )
    filter_horizontal = ("members",)
    inlines = [ConversationMessageInline]


@admin.register(ConversationMessage)
class ConversationMessageAdmin(admin.ModelAdmin):
    list_display = (
        "conversation",
        "created_by",
        "created_at",
    )
    list_filter = (
        "created_at",
    )
    search_fields = (
        "content",
        "created_by__username",
        "conversation__item__name",
    )
    readonly_fields = (
        "created_at",
    )
    filter_horizontal = ("read_by",)