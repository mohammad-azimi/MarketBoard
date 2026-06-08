from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Item(models.Model):
    CONDITION_NEW = "new"
    CONDITION_LIKE_NEW = "like_new"
    CONDITION_USED = "used"
    CONDITION_NEEDS_REPAIR = "needs_repair"

    CONDITION_CHOICES = [
        (CONDITION_NEW, "New"),
        (CONDITION_LIKE_NEW, "Like New"),
        (CONDITION_USED, "Used"),
        (CONDITION_NEEDS_REPAIR, "Needs Repair"),
    ]

    Category = models.ForeignKey(
        Category,
        related_name="items",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    condition = models.CharField(
        max_length=20,
        choices=CONDITION_CHOICES,
        default=CONDITION_USED,
    )
    location = models.CharField(max_length=120, blank=True, default="")
    image = models.ImageField(upload_to="item_images", blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User,
        related_name="items",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        related_name="favorites",
        on_delete=models.CASCADE,
    )
    item = models.ForeignKey(
        Item,
        related_name="favorited_by",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
        constraints = [
            models.UniqueConstraint(
                fields=("user", "item"),
                name="unique_user_favorite_item",
            )
        ]

    def __str__(self):
        return f"{self.user.username} saved {self.item.name}"