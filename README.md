# iris-image-classification
Iris Image data set classification using python

# Building python code
On windows, download anaconda and run the python code in anaconda pyhon prompt
For other linux based distributions, run pip install -r requirements.txt and then run the python files
Please see the docker file for more info

# Build and Run as a docker image locally
Comment out the proxy settings in the docker file
Build and run the docker image using the commands
cd /python/iris-image-classification
docker build -t iris-model .
docker run --rm -p 8080:8080 iris-model

# Running the app from a public docker repository
Go to https://hub.docker.com/r/vishwa787/iris-model
Pull the docker image using the command "docker pull vishwa787/iris-model"
docker run --rm -p 8080:8080 iris-model

# Building the frontend code
To be filled up 

# Building the frontend + Backend code
To be filled up for testing
