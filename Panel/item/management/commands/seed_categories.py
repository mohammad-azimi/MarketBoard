from django.core.management.base import BaseCommand

from item.models import Category


class Command(BaseCommand):
    help = "Create default marketplace categories"

    def handle(self, *args, **options):
        categories = [
            "Electronics",
            "Furniture",
            "Clothing",
            "Books",
            "Sports",
            "Vehicles",
            "Home",
            "Other",
        ]

        created_count = 0

        for name in categories:
            _, created = Category.objects.get_or_create(name=name)

            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Default categories ready. Created {created_count} new categories."
            )
        )