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


class NewItemForm(forms.ModelForm):
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
                    "min": "0",
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
                }
            ),
        }


class EditItemForm(forms.ModelForm):
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
                    "min": "0",
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
                }
            ),
            "is_sold": forms.CheckboxInput(
                attrs={
                    "class": CHECKBOX_CLASSES,
                }
            ),
        }