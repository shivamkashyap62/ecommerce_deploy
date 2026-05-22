# Use an official lightweight Python image
FROM python:3.12-slim

# Set build-time environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies required for package compilation and Pillow
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the entire workspace into the docker image
COPY . /app/

# Expose the application port
EXPOSE 8000

# Create a non-privileged system user for running the application securely
RUN useradd -u 1000 django && \
    mkdir -p /app/clothes_donation/staticfiles /app/clothes_donation/media && \
    chown -R django:django /app

# Switch to the non-root user
USER django

# Run collectstatic to prepare production static assets
# (Uses empty env vars just to bypass decoupling errors during build phase)
RUN SECRET_KEY=build-time-key-only DEBUG=False ALLOWED_HOSTS=localhost python clothes_donation/manage.py collectstatic --noinput

# Start the application: automatically run migrations first, then start Gunicorn
CMD ["sh", "-c", "python /app/clothes_donation/manage.py migrate --noinput && gunicorn --bind 0.0.0.0:8000 --chdir /app/clothes_donation clothes_donation.wsgi:application"]
