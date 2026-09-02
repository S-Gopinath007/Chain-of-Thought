# Use a lightweight stable Python image
FROM python:3.11-slim

# Prevent Python from writing .pyc files and force unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establish working directory inside the container
WORKDIR /app

# Install system dependencies needed for runtime subprocesses
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    coreutils \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies directly 
RUN pip install --no-cache-dir google-genai python-dotenv

# Copy all source files from your local directory into the container
COPY main.py prompts.py environment.py eval.py ./

# Execute the orchestrator pipeline when the container boots
CMD ["python", "main.py"]
