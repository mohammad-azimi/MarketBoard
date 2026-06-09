# MarketBoard

MarketBoard is a Django-based classified ads marketplace where users can create accounts, publish item listings, browse available products, search and filter listings, save favorite items, contact sellers through an internal messaging system, and manage their own marketplace activity from a personal dashboard.

This project started as a Django learning project and has been improved into a cleaner, more portfolio-ready full-stack web application.

## Features

* User registration, login, and logout
* Create, update, and delete marketplace listings
* Listing delete confirmation page
* Image upload support for listings
* Search listings by keyword
* Filter listings by category
* Filter listings by condition
* Filter listings by minimum and maximum price
* Sort listings by newest, oldest, price, name, and popularity
* Pagination for marketplace listings
* Item detail pages with related listings
* Seller profile pages with seller statistics
* Favorite / saved listings system
* User dashboard for managing personal listings
* Dashboard analytics for listings, sold items, saved items, and total views
* Listing view tracking
* Internal conversation system between buyers and sellers
* Inbox page with latest message previews
* Unread message tracking and navigation badge
* Form validation for price, description, location, and image upload
* Custom 403, 404, and 500 error pages
* Demo data seeding commands
* Environment-based Django configuration
* Production-ready static file configuration with WhiteNoise

## Tech Stack

* Python
* Django
* SQLite
* HTML
* Tailwind CSS
* Pillow
* python-dotenv
* WhiteNoise

## Project Structure

```text
MarketBoard/
├── Panel/
│   ├── Panel/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── conversation/
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── admin.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── core/
│   │   ├── templates/
│   │   ├── context_processors.py
│   │   ├── forms.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── dashboard/
│   │   ├── templates/
│   │   ├── urls.py
│   │   └── views.py
│   ├── item/
│   │   ├── management/
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── admin.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/mohammad-azimi/MarketBoard.git
cd MarketBoard
```

### 2. Create and activate a virtual environment

On Windows:

```bash
python -m venv env
env\Scripts\activate
```

On macOS/Linux:

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create environment variables

Create a `.env` file in the project root using `.env.example` as a template:

```env
DJANGO_SECRET_KEY=change-this-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

DJANGO_CSRF_TRUSTED_ORIGINS=
DJANGO_SECURE_SSL_REDIRECT=False
DJANGO_SESSION_COOKIE_SECURE=False
DJANGO_CSRF_COOKIE_SECURE=False
```

### 5. Apply database migrations

```bash
cd Panel
python manage.py migrate
```

### 6. Seed default categories

```bash
python manage.py seed_categories
```

### 7. Optional: seed demo marketplace data

```bash
python manage.py seed_demo_data
```

Demo account:

```text
username: demo_seller
password: demo12345
```

### 8. Start the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Useful Commands

Run migrations:

```bash
python manage.py migrate
```

Create default categories:

```bash
python manage.py seed_categories
```

Create demo data:

```bash
python manage.py seed_demo_data
```

Create an admin user:

```bash
python manage.py createsuperuser
```

Collect static files:

```bash
python manage.py collectstatic --noinput
```

Run system checks:

```bash
python manage.py check
```

## Main Pages

* **Home Page** — marketplace overview, statistics, latest listings, popular listings, and categories
* **Browse Items** — search, filter, sort, and paginate available listings
* **Item Detail Page** — view listing information, seller, views, related items, save listing, and contact seller
* **Seller Profile Page** — view seller statistics and active listings
* **Dashboard** — manage personal listings, saved items, and listing analytics
* **Inbox** — view conversations with buyers and sellers
* **Conversation Detail Page** — send and read marketplace messages
* **New Item Page** — create a new marketplace listing
* **Edit Item Page** — update an existing listing and mark it as sold
* **Delete Confirmation Page** — safely confirm listing deletion
* **Authentication Pages** — sign up, log in, and log out
* **Custom Error Pages** — 403, 404, and 500 pages

## Environment Variables

| Variable                       | Description                                            | Example                   |
| ------------------------------ | ------------------------------------------------------ | ------------------------- |
| `DJANGO_SECRET_KEY`            | Secret key used by Django                              | `change-this-secret-key`  |
| `DJANGO_DEBUG`                 | Enables or disables debug mode                         | `True`                    |
| `DJANGO_ALLOWED_HOSTS`         | Comma-separated list of allowed hosts                  | `127.0.0.1,localhost`     |
| `DJANGO_CSRF_TRUSTED_ORIGINS`  | Comma-separated list of trusted origins for deployment | `https://your-domain.com` |
| `DJANGO_SECURE_SSL_REDIRECT`   | Redirect HTTP to HTTPS in production                   | `False`                   |
| `DJANGO_SESSION_COOKIE_SECURE` | Send session cookies only over HTTPS                   | `False`                   |
| `DJANGO_CSRF_COOKIE_SECURE`    | Send CSRF cookies only over HTTPS                      | `False`                   |

## Screenshots

Screenshots should be added after the final UI review.

Recommended screenshots:

* Home page
* Browse listings page
* Item detail page
* Seller profile page
* Dashboard
* Inbox
* Create listing form

## What I Learned

Through this project, I practiced:

* Building a multi-app Django project
* Working with Django models, views, forms, templates, and URLs
* Implementing authentication and user-specific data
* Handling image uploads with Pillow
* Creating custom model validation in forms
* Building search, filtering, sorting, and pagination
* Using Django messages for user feedback
* Creating a favorites system
* Building an internal messaging system
* Tracking unread messages
* Adding dashboard analytics
* Managing environment variables with python-dotenv
* Preparing static files for deployment with WhiteNoise
* Cleaning a repository for a better GitHub portfolio presentation

## Current Status

MarketBoard is a portfolio-ready Django marketplace project with core marketplace functionality, user dashboards, internal messaging, analytics, demo data, custom error pages, and production-oriented settings.

Planned improvements:

* Deployment to a live hosting platform
* More advanced image handling
* Public user profile customization
* Email notifications for messages
* Better conversation search
* Optional PostgreSQL support for production
* Automated tests

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
