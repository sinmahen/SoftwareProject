# ============================================
# Dockerfile - Python FastAPI Calculator API
# ============================================

FROM python:3.11-slim

# Create non-root user for security
RUN groupadd -g 1001 appgroup && \
    useradd -u 1001 -g appgroup appuser

WORKDIR /app

# Install OS dependencies (curl required for healthcheck)
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

# Set ownership to non-root user
RUN chown -R appuser:appgroup /app

USER appuser

# Application port (FastAPI runs on 8000)
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Start FastAPI with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
