FROM python:3.6-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /api

#Sets the working directory in the image
WORKDIR /api
#copy the contents in the content directory into the /api in the image
COPY . /api

RUN pip install --trusted-host pypi.python.org -r requirements.txt



EXPOSE 8000


CMD ["python", "manage.py", "runserver"]