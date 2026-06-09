import os

from django import forms

from .models import Item


INPUT_CLASSES = (
    "w-full rounded-2xl border border-white/10 bg-slate-950/80 px-4 py-3 "
    "text-sm text-white outline-none transition placeholder:text-slate-500 "
    "focus:border-cyan-400"
)

CHECKBOX_CLASSES = (
    "h-5 w-5 rounded border-white/10 bg-slate-950 text-cyan-400 "
    "focus:ring-cyan-400"
)

ALLOWED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
MAX_IMAGE_SIZE_MB = 5
MAX_IMAGE_SIZE_BYTES = MAX_IMAGE_SIZE_MB * 1024 * 1024


class BaseItemForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()

        if len(name) < 3:
            raise forms.ValidationError("Listing name must be at least 3 characters long.")

        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")

        if description:
            description = description.strip()

            if len(description) < 10:
                raise forms.ValidationError(
                    "Description must be at least 10 characters long."
                )

        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")

        if price is None:
            raise forms.ValidationError("Price is required.")

        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")

        return price

    def clean_location(self):
        location = self.cleaned_data.get("location", "").strip()

        if location and len(location) < 2:
            raise forms.ValidationError("Location must be at least 2 characters long.")

        return location

    def clean_image(self):
        image = self.cleaned_data.get("image")

        if not image:
            return image

        extension = os.path.splitext(image.name)[1].lower()

        if extension not in ALLOWED_IMAGE_EXTENSIONS:
            allowed_extensions = ", ".join(sorted(ALLOWED_IMAGE_EXTENSIONS))
            raise forms.ValidationError(
                f"Unsupported image format. Allowed formats: {allowed_extensions}."
            )

        if image.size > MAX_IMAGE_SIZE_BYTES:
            raise forms.ValidationError(
                f"Image size must be less than {MAX_IMAGE_SIZE_MB} MB."
            )

        return image


class NewItemForm(BaseItemForm):
    class Meta:
        model = Item
        fields = (
            "Category",
            "name",
            "description",
            "price",
            "condition",
            "location",
            "image",
        )

        labels = {
            "Category": "Category",
            "name": "Listing Name",
            "description": "Description",
            "price": "Price",
            "condition": "Condition",
            "location": "Location",
            "image": "Listing Image",
        }

        help_texts = {
            "description": "Write a clear description with the most important details.",
            "price": "Use a positive number. Example: 120 or 89.99.",
            "location": "Optional. Example: Saint Petersburg.",
            "image": f"Optional. Allowed formats: JPG, PNG, WEBP. Max size: {MAX_IMAGE_SIZE_MB} MB.",
        }

        widgets = {
            "Category": forms.Select(
                attrs={
                    "class": INPUT_CLASSES,
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Example: iPhone 13 Pro",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Describe the item, its condition, and any important details.",
                    "rows": 7,
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Example: 450",
                    "min": "0.01",
                    "step": "0.01",
                }
            ),
            "condition": forms.Select(
                attrs={
                    "class": INPUT_CLASSES,
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Example: Saint Petersburg",
                }
            ),
            "image": forms.FileInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "accept": ".jpg,.jpeg,.png,.webp,image/jpeg,image/png,image/webp",
                }
            ),
        }


class EditItemForm(BaseItemForm):
    class Meta:
        model = Item
        fields = (
            "Category",
            "name",
            "description",
            "price",
            "condition",
            "location",
            "image",
            "is_sold",
        )

        labels = {
            "Category": "Category",
            "name": "Listing Name",
            "description": "Description",
            "price": "Price",
            "condition": "Condition",
            "location": "Location",
            "image": "Listing Image",
            "is_sold": "Mark this listing as sold",
        }

        help_texts = {
            "description": "Write a clear description with the most important details.",
            "price": "Use a positive number. Example: 120 or 89.99.",
            "location": "Optional. Example: Saint Petersburg.",
            "image": f"Optional. Allowed formats: JPG, PNG, WEBP. Max size: {MAX_IMAGE_SIZE_MB} MB.",
            "is_sold": "Sold listings will not appear in the public marketplace browse page.",
        }

        widgets = {
            "Category": forms.Select(
                attrs={
                    "class": INPUT_CLASSES,
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Example: iPhone 13 Pro",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Describe the item, its condition, and any important details.",
                    "rows": 7,
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Example: 450",
                    "min": "0.01",
                    "step": "0.01",
                }
            ),
            "condition": forms.Select(
                attrs={
                    "class": INPUT_CLASSES,
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "placeholder": "Example: Saint Petersburg",
                }
            ),
            "image": forms.FileInput(
                attrs={
                    "class": INPUT_CLASSES,
                    "accept": ".jpg,.jpeg,.png,.webp,image/jpeg,image/png,image/webp",
                }
            ),
            "is_sold": forms.CheckboxInput(
                attrs={
                    "class": CHECKBOX_CLASSES,
                }
            ),
        }