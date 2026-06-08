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