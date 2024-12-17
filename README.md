# Social Media API

A Django project for creating a simple social media API that allows users to create, update, and delete posts, follow other users, and view a feed of posts.

## Features

- CRUD operations for users and posts.
- Follow/unfollow functionality for users.
- Display posts from followed users in a feed.

## Installation

Follow these steps to set up and run the project locally:

```bash
# Clone the repository
git clone https://github.com/FatmaElzhraaAbuKhdra/social_media_api.git
cd social_media_api

# Create and activate a virtual environment
python -m venv env
source env/bin/activate  # For Linux or Mac
env\Scripts\activate     # For Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
```
