# Python 3.8 Alphine Lightweight docker image
FROM python:3.8-alpine

# Python should be unbuffered in an image
ENV PYTHONUNBUFFERED 1

# Copy requirements.txt from host to image
COPY ./requirements.txt /requirements.txt 
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
# Install dependencies via pip 
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps
# Run below command
RUN mkdir /app
# Set the default working directory to /app
WORKDIR /app
# Copy Source code from host to image
COPY ./app /app

# Add a user for security purpose
RUN adduser -D rounak
# Set the current user to the above created user
USER rounak