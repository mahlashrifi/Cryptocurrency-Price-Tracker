# Stage 1: Build the application
FROM python:3.9-alpine AS builder

WORKDIR /app

# # Install build dependencies
# RUN apk add --no-cache --virtual .build-deps gcc musl-dev

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --user -r requirements.txt

# Stage 2: Build the final image
FROM python:3.9-alpine

WORKDIR /app

# Copy from builder image
COPY --from=builder /root/.local /usr/local

# Copy source code
COPY . .

COPY ../shared ./shared

# Expose port for the FastAPI application
EXPOSE 8000

# Uvicorn will listen on this port and this host
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
