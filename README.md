# Gather-Up

Gather-Up is a social media platform for discovering and sharing events.  
Users can create accounts, post events, browse upcoming activities, search and filter events, and indicate attendance by liking events.

The platform is built using Django and Django REST Framework, providing a structured and scalable backend for event management and user interaction.

---

## Features

- User authentication (Sign up / Login / Logout)
- Create, edit, and delete events
- Upload images for events
- Search functionality
- Event filtering
- Like system to indicate attendance
- Display number of users attending an event
- REST API powered by Django REST Framework

---

## Tech Stack

- Python
- Django
- Django REST Framework
- Pillow (image handling)
- Docker
- Azure Pipelines (CI/CD)

---

## Installation

### Option 1 – Run Locally (Development)

1. Clone the repository:

git clone https://github.com/Ladinski/Gather-Up.git

cd Gather-Up

2. Create and activate a virtual environment:


python -m venv venv

Activate the virtual enviroment

3. Install dependencies:


pip install -r requirements.txt

4. Apply migrations:


python manage.py migrate



---

## How It Works

1. Users create an account and log in.
2. Authenticated users can:
   - Post new events
   - Upload event images
   - Browse events
   - Search and filter events
   - Like events to indicate attendance
3. The number of likes represents how many users are attending an event.

---

## API

Gather-Up provides RESTful endpoints using Django REST Framework.

Core capabilities include:

- Retrieve events
- Create new events
- Update existing events
- Delete events
- Like and unlike events

API documentation can be expanded as the project evolves.

---

## Development Notes

- Uses Django’s built-in authentication system.
- Media uploads handled via Pillow.
- Containerized with Docker for consistent environments.
- CI/CD configured using Azure Pipelines.

---

## Future Improvements

- Event categories
- Comments on events
- Notifications system
- Enhanced user profiles
- Production deployment configuration

