.PHONY: backend-check backend-test backend-migrate frontend-build

backend-check:
	cd backend && python manage.py check

backend-test:
	cd backend && python manage.py test

backend-migrate:
	cd backend && python manage.py makemigrations --check --dry-run

frontend-build:
	cd frontend && npm run build
