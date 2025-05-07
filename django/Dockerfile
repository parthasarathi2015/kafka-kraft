# Use Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy Django project
COPY . /app/

COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run Django server
CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]
