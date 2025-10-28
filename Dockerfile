# Dockerfile for Hugging Face Spaces Deployment
# PublicSource Classification Testing Tool Backend

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better Docker layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download spaCy English model
RUN python -m spacy download en_core_web_sm

# Copy all application files
COPY . .

# Create necessary directories
RUN mkdir -p /tmp/test_classification_uploads

# Expose port 5001 (Hugging Face Spaces standard port 7860 will be remapped)
EXPOSE 7860

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=7860

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:7860/api/health')"

# Run the application on port 7860 (Hugging Face standard)
CMD ["python", "backend/test_api.py"]
