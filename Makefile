
venv:
	# create a virtual environment
	conda create -n RL-environment python=3.9 anaconda

activate:
	# activate venv
	bash -c "source .venv/bin/activate"

install:
	# install commands
	conda update conda &&\
		pip --no-cache-dir install -r requirements.txt

build:
	# build the container: More important for the CI/CD
	
	
run:
	# run the container
	

all: venv activate install build