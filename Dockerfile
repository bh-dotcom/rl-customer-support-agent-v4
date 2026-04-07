# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install server dependencies
RUN pip install --no-cache-dir -r server/requirements.txt

# Install frontend dependencies
RUN pip install --no-cache-dir -r frontend/requirements.txt

# Expose port for FastAPI and Streamlit
EXPOSE 8000
EXPOSE 8501

# Start FastAPI (server) & Streamlit (frontend)
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "8000"]
