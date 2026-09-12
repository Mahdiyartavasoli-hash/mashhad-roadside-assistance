# Django Backend

## Commands

```bash
python manage.py migrate
python manage.py seed_demo
python manage.py createsuperuser
python manage.py runserver
```

Production checks:

```bash
python manage.py check --deploy
python manage.py test
python manage.py collectstatic --noinput
```

## Public endpoints

- `GET /api/health/`
- `GET /api/site/`
- `GET /api/blog/`
- `GET /api/blog/<slug>/`
- `POST /api/leads/`

Public lead creation is throttled. Admin access remains protected by Django authentication.
