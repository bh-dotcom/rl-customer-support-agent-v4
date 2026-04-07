# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install server and frontend dependencies
RUN pip install --no-cache-dir -r server/requirements.txt
RUN pip install --no-cache-dir -r frontend/requirements.txt

# Expose ports
EXPOSE 8000 8501

# Start FastAPI server by default
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "8000"]
