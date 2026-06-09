from conversation.models import ConversationMessage


def unread_messages_count(request):
    if not request.user.is_authenticated:
        return {
            "unread_messages_count": 0,
        }

    count = (
        ConversationMessage.objects.filter(
            conversation__members=request.user,
        )
        .exclude(
            created_by=request.user,
        )
        .exclude(
            read_by=request.user,
        )
        .distinct()
        .count()
    )

    return {
        "unread_messages_count": count,
    }