FROM python:3.9

# Update package lists and install necessary dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# Ensure pip is updated
RUN pip3 install --upgrade pip

# Install Flask
RUN pip3 install flask

# Copy project files into the container
COPY . /opt/

# Set working directory to /opt
WORKDIR /opt/

# Run the application
CMD ["python3", "app.py"]

