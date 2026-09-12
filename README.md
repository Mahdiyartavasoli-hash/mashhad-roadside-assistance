# Mashhad Roadside Assistance — Full Stack

Production-oriented starter for a 24/7 Mashhad roadside-assistance business.

## Stack

- Frontend: semantic HTML5, Tailwind CSS 4, Vanilla JavaScript
- Backend: Django 6.0, Django REST Framework 3.18
- Database: PostgreSQL in production; SQLite fallback for local development
- Static files: WhiteNoise
- Production WSGI: Gunicorn
- Deployment: frontend can be hosted on Vercel; Django API can be hosted on Vercel or another Python host; PostgreSQL should be a managed database in production.

Current official references: Django 6.0 docs, DRF 3.18.x release notes, and Tailwind's v4 CLI workflow. See the links in the project notes below.

## Project structure

```text
frontend/   Static site + Tailwind + Vanilla JS
backend/    Django project + REST API + CMS/Admin
```

## Local development — easiest

### 1. Backend with SQLite

```bash
cd backend
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env   # Windows PowerShell: Copy-Item .env.example .env
python manage.py migrate
python manage.py seed_demo
python manage.py createsuperuser
python manage.py runserver
```

API: `http://127.0.0.1:8000/api/health/`
Admin: `http://127.0.0.1:8000/admin/`

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

For a production CSS build:

```bash
npm run build
```

The frontend defaults to `/api`. If frontend and backend are on different origins, edit `frontend/src/js/config.js` and set `apiBase` to the public API URL, then configure CORS/CSRF accordingly.

## PostgreSQL with Docker

From the repository root:

```bash
docker compose up --build
```

The API will be available at `http://127.0.0.1:8000`.

## CMS

Django Admin manages:

- Site settings and contact information
- SEO settings
- Services
- Vehicle categories
- Blog posts in Persian and English
- FAQ
- Testimonials
- Statistics
- Assistance requests/leads

The frontend is data-driven and falls back to local content if the API is unavailable.

## Production checklist

Before launch, replace every placeholder:

- brand name
- phone and WhatsApp
- domain and canonical URLs
- logo and real images
- real statistics
- real customer reviews
- real business hours
- final Persian/English copy
- real SEO metadata
- real social/share image

Then:

```bash
python manage.py check --deploy
python manage.py test
python manage.py collectstatic --noinput
```

Never deploy with `DEBUG=1`, never commit `.env`, and use a strong unique `DJANGO_SECRET_KEY`.

## Deployment architecture

Recommended:

```text
Browser
  |
  +--> Vercel / static frontend
  |
  +--> Django API
          |
          +--> PostgreSQL
          +--> Media storage
```

A single-origin Django deployment is also possible later by serving the compiled frontend through the Django application.

## Important SEO note

`example.com` values are intentionally placeholders. Replace them before production and generate the final sitemap for the real domain. LocalBusiness/AutomotiveBusiness structured data should only contain verified business information.
