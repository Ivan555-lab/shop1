# Pull base image
FROM python:3.10
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /a3
# Install dependencies
COPY Pipfile Pipfile.lock /a3/
RUN pip install pipenv && pipenv install --system
# Copy project
COPY . /a3/
