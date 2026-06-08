from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from item.models import Item

from .forms import ConversationMessageForm
from .models import Conversation


@login_required
def inbox(request):
    conversations = (
        request.user.conversations.all()
        .select_related(
            "item",
            "item__Category",
            "item__created_by",
        )
        .prefetch_related(
            "members",
            "messages",
            "messages__created_by",
            "messages__read_by",
        )
    )

    for conversation in conversations:
        conversation_messages = list(conversation.messages.all())
        conversation.latest_message = (
            conversation_messages[-1] if conversation_messages else None
        )

        unread_count = 0

        for conversation_message in conversation_messages:
            read_user_ids = {
                user.id for user in conversation_message.read_by.all()
            }

            if (
                conversation_message.created_by_id != request.user.id
                and request.user.id not in read_user_ids
            ):
                unread_count += 1

        conversation.unread_count = unread_count

    return render(
        request,
        "conversation/inbox.html",
        {
            "conversations": conversations,
        },
    )


@login_required
def new(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        messages.warning(
            request,
            "You cannot start a conversation about your own listing.",
        )
        return redirect("item:detail", pk=item_pk)

    conversations = Conversation.objects.filter(item=item).filter(
        members__in=[request.user]
    )

    if conversations.exists():
        messages.info(
            request,
            "You already have a conversation for this listing.",
        )
        return redirect("conversation:detail", pk=conversations.first().id)

    if request.method == "POST":
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            conversation_message.read_by.add(request.user)

            messages.success(
                request,
                "Message sent successfully.",
            )
            return redirect("conversation:detail", pk=conversation.id)
    else:
        form = ConversationMessageForm()

    return render(
        request,
        "conversation/new.html",
        {
            "form": form,
            "item": item,
        },
    )


@login_required
def detail(request, pk):
    conversation = get_object_or_404(
        Conversation.objects.prefetch_related(
            "messages",
            "messages__created_by",
            "messages__read_by",
        ),
        members__in=[request.user],
        pk=pk,
    )

    unread_messages = (
        conversation.messages.exclude(created_by=request.user)
        .exclude(read_by=request.user)
    )

    for unread_message in unread_messages:
        unread_message.read_by.add(request.user)

    if request.method == "POST":
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            conversation_message.read_by.add(request.user)

            conversation.save()

            messages.success(
                request,
                "Reply sent successfully.",
            )
            return redirect("conversation:detail", pk=pk)
    else:
        form = ConversationMessageForm()

    return render(
        request,
        "conversation/detail.html",
        {
            "conversation": conversation,
            "form": form,
        },
    )