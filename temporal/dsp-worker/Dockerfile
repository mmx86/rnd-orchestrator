# 3.13 had not full support yet [jan 2015].
# https://github.com/temporalio/sdk-python/issues/672
FROM python:3.12-slim-bookworm

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
