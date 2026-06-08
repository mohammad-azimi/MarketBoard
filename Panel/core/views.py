from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import redirect, render

from item.models import Category, Item

from .forms import SignupForm


def index(request):
    items = (
        Item.objects.filter(is_sold=False)
        .select_related("Category", "created_by")
        .order_by("-created_at")[:6]
    )

    popular_items = (
        Item.objects.filter(is_sold=False)
        .select_related("Category", "created_by")
        .order_by("-views_count", "-created_at")[:3]
    )

    categories = Category.objects.all()

    total_listings = Item.objects.count()
    active_listings = Item.objects.filter(is_sold=False).count()
    sold_listings = Item.objects.filter(is_sold=True).count()
    total_categories = categories.count()
    total_users = User.objects.count()
    total_views = Item.objects.aggregate(total=Sum("views_count"))["total"] or 0

    return render(
        request,
        "core/index.html",
        {
            "categories": categories,
            "items": items,
            "popular_items": popular_items,
            "total_listings": total_listings,
            "active_listings": active_listings,
            "sold_listings": sold_listings,
            "total_categories": total_categories,
            "total_users": total_users,
            "total_views": total_views,
        },
    )


def contact(request):
    return render(request, "core/contact.html")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                "Account created successfully. Welcome to MarketBoard.",
            )

            return redirect("item:items")
    else:
        form = SignupForm()

    return render(
        request,
        "core/signup.html",
        {
            "form": form,
        },
    )


def permission_denied_view(request, exception=None):
    return render(
        request,
        "core/403.html",
        status=403,
    )


def page_not_found_view(request, exception=None):
    return render(
        request,
        "core/404.html",
        status=404,
    )


def server_error_view(request):
    return render(
        request,
        "core/500.html",
        status=500,
    )