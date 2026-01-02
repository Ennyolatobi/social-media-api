# Social Media API

## 📌 Project Overview
Social Media API is a backend RESTful service built with Django and Django REST Framework.  
It provides core social media features such as user management, posts, following, personalized feeds, and likes.

This project focuses on backend functionality and API design. There is no frontend interface.

---

## 🚀 Features

### Functional Requirements
- User authentication
- Create posts
- Follow and unfollow users
- Personalized feed (posts from followed users)
- Like posts

### Technical Requirements
- Django & Django REST Framework
- SQLite database
- Session-based authentication
- RESTful API endpoints

### Stretch Features
- Post likes
- Media field support
- Profile customization fields

---

## 🧩 API Endpoints

| Method | Endpoint | Description |
|------|--------|------------|
| GET | `/api/users/all/` | List all users |
| POST | `/api/users/follow/<id>/` | Follow a user |
| POST | `/api/users/unfollow/<id>/` | Unfollow a user |
| POST | `/api/posts/` | Create a post |
| GET | `/api/feed/` | View personalized feed |
| POST | `/api/like/<post_id>/` | Like a post |

---

## 🧪 Testing the API

The API can be tested using `curl` or any API client.

### Example: Create a post
```bash
curl -X POST http://127.0.0.1:8000/api/posts/ \
  -u username:password \
  -H "Content-Type: application/json" \
  -d '{"content": "Hello world"}'

---

## 📂 Project Structure
social-media-api/
│
├── backend/
│ ├── backend/
│ │ ├── settings.py
│ │ ├── urls.py
│ │ └── wsgi.py
│ ├── users/
│ ├── posts/
│ ├── manage.py
│
├── venv/
├── .gitignore
└── README.md

✍️ Author

Eniola Omoniyi
Backend Engineering Student

GitHub: https://github.com/Ennyolatobi