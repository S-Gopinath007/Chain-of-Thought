FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    coreutils \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir google-genai python-dotenv

COPY main.py prompts.py environment.py eval.py ./

CMD ["python", "main.py"]
