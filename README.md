# GK Technologies Backend

This is the backend API for the GK Technologies website. Built with Django and Django REST Framework.

## Features

- User Management
- Product Catalog
- Career Portal
- News & Updates
- API Documentation with Swagger/ReDoc
- JWT Authentication
- File Upload Support
- Filtering, Searching, and Ordering
- Environment-based Settings

## Setup

1. Clone the repository
```bash
git clone https://github.com/Teja2142/Gktech-backend.git
cd Gktech-backend
```

2. Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create .env file and set environment variables (see .env.example)

5. Run migrations
```bash
python manage.py migrate
```

6. Create superuser
```bash
python manage.py createsuperuser
```

7. Run the development server
```bash
python manage.py runserver
```

## API Documentation

Once the server is running, you can access:
- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/

## API Endpoints

### Users
- `POST /api/v1/users/` - Register new user
- `GET /api/v1/users/` - List users (admin only)
- `GET /api/v1/users/{id}/` - Get user details
- `PUT /api/v1/users/{id}/` - Update user
- `DELETE /api/v1/users/{id}/` - Delete user

### Products
- `GET /api/v1/products/` - List products
- `GET /api/v1/products/{id}/` - Get product details
- `POST /api/v1/products/` - Create product (admin only)
- `PUT /api/v1/products/{id}/` - Update product (admin only)
- `DELETE /api/v1/products/{id}/` - Delete product (admin only)
- `GET /api/v1/products/categories/` - List categories

### Careers
- `GET /api/v1/careers/jobs/` - List job postings
- `POST /api/v1/careers/jobs/` - Create job posting (admin only)
- `GET /api/v1/careers/jobs/{id}/` - Get job details
- `POST /api/v1/careers/applications/` - Submit job application
- `GET /api/v1/careers/applications/` - List applications (admin only)

### News
- `GET /api/v1/news/` - List news articles
- `GET /api/v1/news/{slug}/` - Get article details
- `POST /api/v1/news/` - Create article (admin only)
- `PUT /api/v1/news/{slug}/` - Update article (admin only)
- `DELETE /api/v1/news/{slug}/` - Delete article (admin only)
- `GET /api/v1/news/categories/` - List news categories

## Development

The project uses different settings for development and production:
- Development: `gktech.settings.development`
- Production: `gktech.settings.production`

## Deployment

1. Set environment variables
2. Install production dependencies
3. Collect static files
4. Run migrations
5. Use gunicorn for production server