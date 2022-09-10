FROM continuumio/miniconda3

WORKDIR /app

# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
RUN echo "conda activate RL-environment" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

RUN echo "Make sure stuff is installed:"
RUN python -c "import gym"
RUN python -c "import matplotlib"
RUN python -c "import numpy"
