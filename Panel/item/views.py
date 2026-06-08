from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EditItemForm, NewItemForm
from .models import Category, Favorite, Item


def items(request):
    query = request.GET.get("query", "")
    category_id = request.GET.get("category", "0")
    sort = request.GET.get("sort", "newest")
    page = request.GET.get("page", 1)

    sort_options = {
        "newest": "-created_at",
        "oldest": "created_at",
        "price_low": "price",
        "price_high": "-price",
        "name": "name",
    }

    order_by = sort_options.get(sort, "-created_at")

    categories = Category.objects.all()
    items_queryset = Item.objects.filter(is_sold=False)

    selected_category_id = 0

    if category_id and category_id != "0":
        try:
            selected_category_id = int(category_id)
            items_queryset = items_queryset.filter(Category_id=selected_category_id)
        except ValueError:
            selected_category_id = 0

    if query:
        items_queryset = items_queryset.filter(
            Q(name__icontains=query)
            | Q(description__icontains=query)
            | Q(location__icontains=query)
        )

    items_queryset = items_queryset.order_by(order_by)

    paginator = Paginator(items_queryset, 6)

    try:
        items_page = paginator.page(page)
    except PageNotAnInteger:
        items_page = paginator.page(1)
    except EmptyPage:
        items_page = paginator.page(paginator.num_pages)

    return render(
        request,
        "item/items.html",
        {
            "items": items_page,
            "page_obj": items_page,
            "query": query,
            "categories": categories,
            "category_id": selected_category_id,
            "sort": sort,
            "total_items": paginator.count,
        },
    )


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    related_items = (
        Item.objects.filter(Category=item.Category, is_sold=False)
        .exclude(pk=pk)
        .order_by("-created_at")[:3]
    )

    is_favorite = False

    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(
            user=request.user,
            item=item,
        ).exists()

    return render(
        request,
        "item/detail.html",
        {
            "item": item,
            "related_items": related_items,
            "is_favorite": is_favorite,
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

            messages.success(
                request,
                "Listing published successfully.",
            )
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

            messages.success(
                request,
                "Listing updated successfully.",
            )
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
        item_name = item.name
        item.delete()

        messages.success(
            request,
            f'"{item_name}" was deleted successfully.',
        )
        return redirect("dashboard:index")

    return render(
        request,
        "item/confirm_delete.html",
        {
            "item": item,
        },
    )


@login_required
def toggle_favorite(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if item.created_by == request.user:
        messages.warning(
            request,
            "You cannot save your own listing.",
        )
        return redirect("item:detail", pk=pk)

    favorite, created = Favorite.objects.get_or_create(
        user=request.user,
        item=item,
    )

    if created:
        messages.success(
            request,
            "Listing saved to your dashboard.",
        )
    else:
        favorite.delete()
        messages.success(
            request,
            "Listing removed from saved items.",
        )

    return redirect("item:detail", pk=pk)