# Build Stage
FROM python:3.9-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /build

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    unixodbc-dev \
    default-libmysqlclient-dev \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements/ ./requirements

RUN pip install --no-cache-dir --target=/build/deps -r requirements/base.txt


# Final Stage
FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /home/instapaw

# Copy installed dependencies from the builder stage
COPY --from=builder /build/deps /usr/local/lib/python3.9/site-packages
COPY --from=builder /build/deps/bin /usr/local/bin

COPY . .

# Runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    unixodbc-dev \
    default-libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8000
