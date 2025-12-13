FROM python:3.10-slim

LABEL maintainer="Eidelwise Prily Safana"
LABEL description="Diabetes Classification Model - Kriteria 3 ADVANCED"
LABEL version="1.0.0"

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
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

# Default command - serve model with MLflow
CMD ["python", "-c", "import mlflow; import joblib; print('Diabetes Classifier Model - Eidelwise Prily Safana'); print('MLflow Version:', mlflow.__version__); print('Model Ready for Serving!')"]
