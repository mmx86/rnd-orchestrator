FROM python:3.13-slim-bookworm

# Install python dependencies.
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --verbose --no-cache-dir -r requirements.txt && \
    rm requirements.txt

## Add app user.
#RUN useradd --user-group --no-log-init app
#USER app

# Set app working directory.
WORKDIR /app

# Copy app.
COPY dsp /app/dsp

# Run app.
CMD ["uvicorn", "dsp.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
