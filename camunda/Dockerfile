FROM python:3.13-slim-bookworm

# Set working directory.
WORKDIR /app

# Install python dependencies.
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt

# Copy application.
COPY dsp dsp

CMD ["sh", "-c", "alembic upgrade head && uvicorn --host 0.0.0.0 --port 8000 --http httptools dsp_spaces.app:app"]
