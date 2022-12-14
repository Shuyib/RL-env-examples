
venv:
	# create a virtual environment
	conda create -n RL-environment python=3.9 anaconda

activate:
	# activate venv run this manually
	conda activate name_of_path_where

deactivate:
	# deactivate venv run this manually
	conda deactivate 

install:
	# install commands
	conda update -n base -c defaults conda &&\
		conda install gym matplotlib numpy 

start-venv:
	# if the environment.yml is available
	conda env create --file environment.yml --prefix ./venv --quiet


docstrings:
	# format docstring
	pyment -w -o numpydoc *.py

format:
	#format code
	black *.py 

lint:
	#flake8 or #pylint
	pylint --disable=R,C *.py

build:
	# build the container: More important for the CI/CD
	docker build -t RL-environment:v1 .
	
run:
	# run the container
	docker run RL-environment:v1

all: venv activate install build run
