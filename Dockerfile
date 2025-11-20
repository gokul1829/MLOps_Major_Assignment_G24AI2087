# Use official Python image
FROM python:3.10-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose port
EXPOSE 5000

# Ensure uploads dir exists and move savedmodel to root
RUN mkdir -p static/uploads

CMD ["python", "app.py"]
