# Use latest Python runtime as a parent image
FROM python:3.9.12-slim-buster

# Meta-data
LABEL maintainer="" \
      description=""

# Set the working directory to /app
WORKDIR /RL


# ensures that the python output is sent to the terminal without buffering
ENV PYTHONUNBUFFERED=TRUE


# Copy the current directory contents into the container at /app
COPY . /RL

# make a virtual environment
RUN conda create -n RL-environment python=3.9 anaconda

# activate virtual environment
CMD source iris-app/bin/activate

# upgrade pip
RUN pip --no-cache-dir install --upgrade pip

# pip install
RUN pip --no-cache-dir install -r /app/requirements.txt

# Make port available to the world outside this container
EXPOSE 5000

# ENTRYPOINT allows us to specify the default executible
ENTRYPOINT ["python"]

# CMD sets default arguments to executable which may be overwritten when using docker run
CMD ["app.py"]
