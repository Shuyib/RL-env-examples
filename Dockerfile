FROM continuumio/miniconda3

# Specify the working directory
WORKDIR /app

# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
RUN echo "conda activate RL-environment" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# Test if the dependecies were installed in virtual environment
RUN echo "Make sure dependecies are installed:"
RUN python -c "import gym"
RUN python -c "import matplotlib"
RUN python -c "import numpy"

# ENTRYPOINT allows us to specify the default executible
ENTRYPOINT ["python"]

# CMD sets default arguments to executable which may be overwritten when using docker run
CMD ["key-concepts-RL-agent.py"]
