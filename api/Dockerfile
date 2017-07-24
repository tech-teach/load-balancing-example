FROM python:3.6
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
WORKDIR /code
COPY . /code
CMD gunicorn app:app.wsgi --workers=4 --bind=0.0.0.0:5000 --pid=pid --worker-class=meinheld.gmeinheld.MeinheldWorker
