from io import BytesIO

from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from PIL import Image, ImageDraw, ImageFont

from item.models import Category, Item


DEFAULT_CATEGORIES = [
    "Electronics",
    "Furniture",
    "Clothing",
    "Books",
    "Sports",
    "Vehicles",
    "Home",
    "Other",
]


DEMO_ITEMS = [
    {
        "category": "Electronics",
        "name": "Wireless Headphones",
        "description": "Comfortable wireless headphones with clean sound, soft ear cushions, and long battery life.",
        "price": 89.99,
        "condition": Item.CONDITION_LIKE_NEW,
        "location": "Saint Petersburg",
        "color": (34, 211, 238),
    },
    {
        "category": "Electronics",
        "name": "Gaming Keyboard",
        "description": "Mechanical gaming keyboard with RGB lighting, fast switches, and a compact layout.",
        "price": 59.50,
        "condition": Item.CONDITION_USED,
        "location": "Moscow",
        "color": (139, 92, 246),
    },
    {
        "category": "Furniture",
        "name": "Modern Desk Chair",
        "description": "Comfortable desk chair for study or work. Adjustable height and clean modern look.",
        "price": 120.00,
        "condition": Item.CONDITION_USED,
        "location": "Saint Petersburg",
        "color": (16, 185, 129),
    },
    {
        "category": "Books",
        "name": "Python Programming Book",
        "description": "A practical Python book for beginners and intermediate learners, with examples and exercises.",
        "price": 24.99,
        "condition": Item.CONDITION_LIKE_NEW,
        "location": "Kazan",
        "color": (245, 158, 11),
    },
    {
        "category": "Sports",
        "name": "City Bicycle",
        "description": "A simple city bicycle suitable for daily rides, commuting, and weekend cycling.",
        "price": 210.00,
        "condition": Item.CONDITION_USED,
        "location": "Saint Petersburg",
        "color": (239, 68, 68),
    },
    {
        "category": "Home",
        "name": "Smart Desk Lamp",
        "description": "Minimal desk lamp with adjustable brightness, perfect for studying and late-night work.",
        "price": 35.00,
        "condition": Item.CONDITION_NEW,
        "location": "Moscow",
        "color": (59, 130, 246),
    },
    {
        "category": "Clothing",
        "name": "Winter Jacket",
        "description": "Warm winter jacket in good condition. Suitable for cold weather and daily use.",
        "price": 75.00,
        "condition": Item.CONDITION_USED,
        "location": "Saint Petersburg",
        "color": (100, 116, 139),
    },
    {
        "category": "Vehicles",
        "name": "Electric Scooter",
        "description": "Compact electric scooter for short city trips. Easy to fold and carry.",
        "price": 280.00,
        "condition": Item.CONDITION_LIKE_NEW,
        "location": "Moscow",
        "color": (20, 184, 166),
    },
]


class Command(BaseCommand):
    help = "Create demo marketplace categories, user, and listings"

    def handle(self, *args, **options):
        user, user_created = User.objects.get_or_create(
            username="demo_seller",
            defaults={
                "email": "demo@example.com",
            },
        )

        if user_created:
            user.set_password("demo12345")
            user.save()

        categories = {}

        for category_name in DEFAULT_CATEGORIES:
            category, _ = Category.objects.get_or_create(name=category_name)
            categories[category_name] = category

        created_count = 0

        for demo_item in DEMO_ITEMS:
            category = categories[demo_item["category"]]

            item, created = Item.objects.get_or_create(
                name=demo_item["name"],
                created_by=user,
                defaults={
                    "Category": category,
                    "description": demo_item["description"],
                    "price": demo_item["price"],
                    "condition": demo_item["condition"],
                    "location": demo_item["location"],
                    "is_sold": False,
                },
            )

            if created:
                image_file = self.create_demo_image(
                    title=demo_item["name"],
                    category=demo_item["category"],
                    color=demo_item["color"],
                )

                item.image.save(
                    f"{self.slugify_filename(demo_item['name'])}.png",
                    image_file,
                    save=True,
                )

                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Demo data ready. Created {created_count} new listings. Demo user: demo_seller / demo12345"
            )
        )

    def create_demo_image(self, title, category, color):
        width = 1200
        height = 900

        image = Image.new("RGB", (width, height), (15, 23, 42))
        draw = ImageDraw.Draw(image)

        accent = color
        dark_accent = tuple(max(channel - 70, 0) for channel in accent)

        for y in range(height):
            ratio = y / height
            red = int((15 * (1 - ratio)) + (dark_accent[0] * ratio))
            green = int((23 * (1 - ratio)) + (dark_accent[1] * ratio))
            blue = int((42 * (1 - ratio)) + (dark_accent[2] * ratio))
            draw.line([(0, y), (width, y)], fill=(red, green, blue))

        draw.rounded_rectangle(
            [80, 80, width - 80, height - 80],
            radius=60,
            outline=(255, 255, 255),
            width=4,
        )

        draw.rounded_rectangle(
            [120, 120, 430, 190],
            radius=35,
            fill=accent,
        )

        try:
            title_font = ImageFont.truetype("arial.ttf", 72)
            category_font = ImageFont.truetype("arial.ttf", 34)
            small_font = ImageFont.truetype("arial.ttf", 28)
        except OSError:
            title_font = ImageFont.load_default()
            category_font = ImageFont.load_default()
            small_font = ImageFont.load_default()

        draw.text(
            (155, 142),
            category.upper(),
            fill=(15, 23, 42),
            font=category_font,
        )

        wrapped_title = self.wrap_text(title, max_chars=18)

        draw.multiline_text(
            (120, 330),
            wrapped_title,
            fill=(255, 255, 255),
            font=title_font,
            spacing=16,
        )

        draw.text(
            (120, height - 160),
            "MarketBoard Demo Listing",
            fill=(226, 232, 240),
            font=small_font,
        )

        buffer = BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)

        return ContentFile(buffer.read())

    def wrap_text(self, text, max_chars):
        words = text.split()
        lines = []
        current_line = ""

        for word in words:
            next_line = f"{current_line} {word}".strip()

            if len(next_line) <= max_chars:
                current_line = next_line
            else:
                lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        return "\n".join(lines)

    def slugify_filename(self, text):
        return (
            text.lower()
            .replace(" ", "-")
            .replace("/", "-")
            .replace("\\", "-")
        )