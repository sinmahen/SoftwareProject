# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies + curl
RUN apt-get update && apt-get install -y curl && \
    pip install --no-cache-dir fastapi uvicorn && \
    rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1

# Start the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
