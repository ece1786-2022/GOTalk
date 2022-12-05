# production
gunicorn --bind 0.0.0.0:5000 --workers=1 server:app

# dev
#flask --app server --debug run
