from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from item.models import Item


@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user).order_by("-created_at")

    favorite_items = (
        Item.objects.filter(favorited_by__user=request.user)
        .select_related("Category", "created_by")
        .order_by("-favorited_by__created_at")
    )

    total_count = items.count()
    active_count = items.filter(is_sold=False).count()
    sold_count = items.filter(is_sold=True).count()
    saved_count = favorite_items.count()

    return render(
        request,
        "dashboard/index.html",
        {
            "items": items,
            "favorite_items": favorite_items,
            "total_count": total_count,
            "active_count": active_count,
            "sold_count": sold_count,
            "saved_count": saved_count,
        },
    )