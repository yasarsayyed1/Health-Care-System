# Dockerfile for Health Care System Django Project
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /app/

# Collect static files
RUN python newproject/manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start server
CMD ["python", "newproject/manage.py", "runserver", "0.0.0.0:8000"]
