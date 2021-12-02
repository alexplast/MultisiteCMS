run:
	gunicorn -b 0.0.0.0:80 app:app & gunicorn --certfile cert/cert.pem --keyfile cert/key.pem -b 0.0.0.0:443 app:app -w3
debug:
	flask run --host 0.0.0.0 --port 443