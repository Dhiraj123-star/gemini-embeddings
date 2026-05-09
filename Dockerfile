# ============================
# Stage 1 Builder
# ============================
FROM python:3.12-slim AS builder

WORKDIR /app

# Install dependencies
COPY requirements.txt . 

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# =============================
# Stage 2 - Final Image
# =============================
FROM python:3.12-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy application code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]
