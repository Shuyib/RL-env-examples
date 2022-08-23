
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

build:
	# build the container: More important for the CI/CD
	
	
run:
	# run the container
	

all: venv activate install build
