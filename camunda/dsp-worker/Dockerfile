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
COPY dsp_worker /app/dsp_worker

# Run app.
CMD ["python", "-m", "dsp_worker"]
