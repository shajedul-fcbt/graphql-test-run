# GraphQL Pilot

A Django-powered GraphQL API for managing users and messages, built with Strawberry Django. This project serves as a learning pilot for implementing GraphQL APIs in Django applications.

## 🎯 Project Purpose

GraphQL Pilot is a message board application that demonstrates:
- GraphQL API implementation with Django
- User management and authentication
- Message posting and retrieval system
- Real-time message querying with pagination
- GraphQL schema design best practices

## ✨ Features

- **User Management**: Create and retrieve users with authentication
- **Message System**: Post, read, and manage messages
- **GraphQL API**: Full GraphQL implementation with queries and mutations
- **Pagination**: Efficient message pagination with limit/offset
- **Read Status**: Track message read status
- **GraphiQL Interface**: Interactive GraphQL playground for development
- **Admin Interface**: Django admin panel for data management

## 🛠️ Tech Stack

- **Backend**: Django 5.2.5
- **GraphQL**: Strawberry Django
- **Database**: SQLite (development)
- **API**: GraphQL with REST Framework integration

## 📋 Requirements

- Python 3.8+
- Django 5.2.5
- strawberry-django
- djangorestframework

## 🚀 Quick Setup

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd graphql-pilot
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install django==5.2.5
pip install strawberry-django
pip install djangorestframework
```

### 4. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

The application will be available at:
- **GraphQL Endpoint**: http://localhost:8000/graphql/
- **GraphiQL Interface**: http://localhost:8000/graphql/ (with interactive playground)
- **Admin Panel**: http://localhost:8000/admin/

## 📖 API Usage

### GraphQL Endpoint
Access the GraphQL API at `/graphql/` with the following operations:

#### Queries
```graphql
# Get all users
query {
  user {
    id
    username
    messages {
      id
      content
      createdAt
    }
  }
}

# Get messages with pagination
query {
  messages(limit: 10, offset: 0) {
    id
    content
    createdAt
    author {
      username
    }
  }
}

# Get specific user by ID
query {
  user(id: "1") {
    id
    username
    messages {
      content
    }
  }
}

# Get specific message by ID
query {
  message(id: "1") {
    id
    content
    author {
      username
    }
    createdAt
  }
}
```

#### Mutations
```graphql
# Create a new user
mutation {
  addUser(username: "john_doe", password: "secure_password") {
    id
    username
  }
}

# Post a new message
mutation {
  postMessage(authorId: "1", content: "Hello, GraphQL!") {
    id
    content
    author {
      username
    }
    createdAt
  }
}
```

## 🗃️ Data Models

### User Model
- `id`: Unique identifier
- `username`: Username for authentication
- `messages`: Related messages posted by the user

### Message Model
- `id`: Unique identifier
- `content`: Message text content
- `author`: Foreign key to User model
- `is_read`: Boolean flag for read status
- `created_at`: Timestamp of creation

## 🔧 Development

### Project Structure
```
graphql-pilot/
├── core/                 # Django project configuration
│   ├── settings.py      # Django settings
│   ├── urls.py          # URL routing
│   └── ...
├── logbook/             # Main application
│   ├── models.py        # Database models
│   ├── schema.py        # GraphQL schema
│   ├── migrations/      # Database migrations
│   └── ...
├── manage.py            # Django management script
└── db.sqlite3          # SQLite database
```

### Running Tests
```bash
python manage.py test
```

### Making Schema Changes
After modifying models:
```bash
python manage.py makemigrations
python manage.py migrate
```

## 🚨 Known Issues

The current implementation has a few minor bugs in the schema that may need attention:
- Line 47 in `schema.py`: `firtst()` should be `first()`
- Line 57 in `schema.py`: `User.from_django(user)` should be `user`
- Line 67 in `schema.py`: `.first()` is called on a single object

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is a learning pilot and is provided as-is for educational purposes.

## 🔗 Useful Links

- [Django Documentation](https://docs.djangoproject.com/)
- [Strawberry Django Documentation](https://strawberry-graphql.github.io/strawberry-django/)
- [GraphQL Documentation](https://graphql.org/learn/)
