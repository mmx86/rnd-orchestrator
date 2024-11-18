FROM python:3.10-slim-bookworm

# Install python dependencies.
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --verbose --no-cache-dir -r requirements.txt && \
    rm requirements.txt

# Add app user.
RUN useradd --user-group --no-log-init app
USER app

# Set app working directory.
WORKDIR /app

# Copy app.
# TODO: fix (dsp/dsp -> dsp).
COPY dsp_spaces /app
COPY dsp_common /app

# Run app.
CMD ["sh", "-c", "python -m dsp"]
