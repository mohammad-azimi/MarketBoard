from django import forms

from .models import ConversationMessage


TEXTAREA_CLASSES = (
    "w-full rounded-2xl border border-white/10 bg-slate-950/80 px-4 py-3 "
    "text-sm text-white outline-none transition placeholder:text-slate-500 "
    "focus:border-cyan-400"
)


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ("content",)

        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": TEXTAREA_CLASSES,
                    "placeholder": "Write your message...",
                    "rows": 5,
                }
            ),
        }