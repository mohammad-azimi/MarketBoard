from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EditItemForm, NewItemForm
from .models import Category, Item


def items(request):
    query = request.GET.get("query", "")
    category_id = request.GET.get("category", "0")

    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False).order_by("-created_at")

    selected_category_id = 0

    if category_id and category_id != "0":
        try:
            selected_category_id = int(category_id)
            items = items.filter(Category_id=selected_category_id)
        except ValueError:
            selected_category_id = 0

    if query:
        items = items.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    return render(
        request,
        "item/items.html",
        {
            "items": items,
            "query": query,
            "categories": categories,
            "category_id": selected_category_id,
        },
    )


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    related_items = (
        Item.objects.filter(Category=item.Category, is_sold=False)
        .exclude(pk=pk)
        .order_by("-created_at")[:3]
    )

    return render(
        request,
        "item/detail.html",
        {
            "item": item,
            "related_items": related_items,
        },
    )


@login_required
def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect("item:detail", pk=item.id)
    else:
        form = NewItemForm()

    return render(
        request,
        "item/form.html",
        {
            "form": form,
            "title": "Create New Listing",
            "button_label": "Publish Listing",
        },
    )


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect("item:detail", pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(
        request,
        "item/form.html",
        {
            "form": form,
            "title": "Edit Listing",
            "button_label": "Save Changes",
        },
    )


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == "POST":
        item.delete()
        return redirect("dashboard:index")

    return redirect("item:detail", pk=pk)