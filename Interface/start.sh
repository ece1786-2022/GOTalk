gunicorn --bind 0.0.0.0:5000 --workers=1 backend:app

flask --app app --debug run