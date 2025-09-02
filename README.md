# GraphQL Pilot

## 🛠️ Tech Stack

- **Backend**: Django 5.2.5
- **GraphQL**: Strawberry Django
- **Database**: SQLite (development)
- **API**: GraphQL with REST Framework integration

## 🚀 Setup

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
