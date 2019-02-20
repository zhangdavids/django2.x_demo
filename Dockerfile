FROM python:3.6

ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /web_service

# Set the working directory to /web_service
WORKDIR /web_service

# Copy the current directory contents into the container at /web_service
ADD . /web_service/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt