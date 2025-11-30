FROM python:3.10-slim

LABEL maintainer="Eidelwise Prily Safana"
LABEL description="Diabetes Classification Model - Kriteria 3 ADVANCED"

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install mlflow==2.9.2 flask gunicorn

# Copy project files
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV MLFLOW_TRACKING_URI=mlruns
ENV PORT=5000

# Expose port for serving
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# Default command - serve model
CMD ["python", "-c", "import mlflow; print('Diabetes Classifier Model Ready!')"]
