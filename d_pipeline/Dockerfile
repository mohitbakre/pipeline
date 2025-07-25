    # Dockerfile

    # Use an official Python runtime as a parent image
    # We choose a slim-buster image for smaller size
    FROM python:3.11-slim-buster

    # Set the working directory in the container
    WORKDIR /app

    # Install Gunicorn, a WSGI HTTP Server for Python web applications.
    # It's recommended for production deployments over Flask's built-in server.
    RUN pip install gunicorn

    # Copy the requirements file into the container at /app
    COPY requirements.txt .

    # Install any needed packages specified in requirements.txt
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy the application code into the container at /app
    COPY . .

    # Expose the port the app runs on
    EXPOSE 8080

    # Define environment variable for the port (Cloud Run uses PORT)
    ENV PORT=8080

    # Run the application using Gunicorn
    # 0.0.0.0 makes it accessible from outside the container
    # app:app refers to the 'app' Flask instance within 'app.py'
    CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]