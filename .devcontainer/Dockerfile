# Use a lightweight Python image
FROM python:3.12-slim

# Install system dependencies (Git is required for many Python tools)
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv (The homework requires this specific tool)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set the working directory
WORKDIR /workspace
