FROM python:3.6-slim

WORKDIR /api
COPY . /api
RUN pip install --trusted-host pypi.python.org -r requirements.txt



EXPOSE 8000


CMD ["python", "manage.py", "runserver"]