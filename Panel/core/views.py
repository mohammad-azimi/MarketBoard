from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render

from item.models import Category, Item

from .forms import SignupForm


def index(request):
    items = Item.objects.filter(is_sold=False).order_by("-created_at")[:6]
    categories = Category.objects.all()

    return render(
        request,
        "core/index.html",
        {
            "categories": categories,
            "items": items,
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