# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy everything into container
COPY . .

# Install dependencies
RUN pip install -r app/requirements.txt

# Expose port
EXPOSE 5001

# Run app
CMD ["python", "app/app.py"]