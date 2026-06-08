# MarketBoard

MarketBoard is a Django-based classified ads marketplace where users can create accounts, publish item listings, browse available products, search and filter listings, and manage their own ads through a personal dashboard.

This project started as a Django learning project and is being improved into a cleaner, more portfolio-ready full-stack web application.

## Features

* User registration and authentication
* Create, update, and delete marketplace listings
* Browse available items on the homepage
* Search listings by keyword
* Filter listings by category
* View detailed item pages
* Display related items on item detail pages
* Manage user-owned listings from a dashboard
* Upload listing images
* Environment-based Django settings
* SQLite database for local development

## Tech Stack

* Python
* Django
* SQLite
* HTML
* Tailwind CSS
* Pillow
* python-dotenv

## Project Structure

```text
MarketBoard/
├── Panel/
│   ├── Panel/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── core/
│   │   ├── templates/
│   │   ├── urls.py
│   │   └── views.py
│   ├── dashboard/
│   │   ├── templates/
│   │   ├── urls.py
│   │   └── views.py
│   ├── item/
│   │   ├── templates/
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
├── .env.example
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
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
```

### 5. Apply database migrations

```bash
cd Panel
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Main Pages

* **Home Page** — displays the latest available marketplace listings
* **Browse Items** — allows users to search and filter listings
* **Item Detail Page** — shows full listing information and related items
* **Dashboard** — lets authenticated users manage their own listings
* **New Item Page** — allows users to create a new marketplace listing
* **Edit Item Page** — allows users to update existing listings
* **Authentication Pages** — includes sign up and login functionality

## Current Status

MarketBoard is currently being improved as a portfolio project.

Completed:

* Core Django marketplace structure
* User authentication
* Item listing system
* Image upload support
* Search and category filtering
* User dashboard for listing management
* Environment-based Django configuration
* Repository cleanup for a cleaner GitHub presentation

Planned improvements:

* Modern user interface redesign
* Improved dashboard statistics
* Listing condition and status fields
* Favorites system
* Better search and sorting options
* Custom error pages
* Production-ready deployment settings

## Screenshots

Screenshots will be added after the UI redesign phase.

## What I Learned

Through this project, I practiced:

* Building a multi-app Django project
* Working with Django models, views, forms, and templates
* Handling user authentication
* Managing user-specific dashboard data
* Uploading and displaying images with Pillow
* Implementing search and category filtering
* Using environment variables for safer configuration
* Preparing a Django project for a cleaner portfolio presentation

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
