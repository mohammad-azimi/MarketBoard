from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from item.models import Item


@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user).order_by("-created_at")

    total_count = items.count()
    active_count = items.filter(is_sold=False).count()
    sold_count = items.filter(is_sold=True).count()

    return render(
        request,
        "dashboard/index.html",
        {
            "items": items,
            "total_count": total_count,
            "active_count": active_count,
            "sold_count": sold_count,
        },
    )