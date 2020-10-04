# Docker example of using serving Huggingface transformer model through flask

This directory contains code to build a docker image and flask app that serves a [huggingface sentiment analysis pipeline](https://huggingface.co/transformers/main_classes/pipelines.html).

## Contents
1. `app.py`:  The implementation of the flask app
2. `DockerFile`
3. `Docker-compose.yml`
4. `preload.py`:  A script to download the transformers weights, executed during image build.
5. `requirements.txt`:  Pip requirements file, installed when the image is built.

## Instructions

Run the following steps from this directory:

Build the image:

`docker build -t transformer_app .`

Start the container:

`docker run -d -p 5000:5000 transformer_app`

See `testing_transapp.ipynb` for an example of using [requests](https://requests.readthedocs.io/en/master/user/quickstart/) to interact with the flask app.

You can also use curl to send text to the app:

`curl -X POST http://127.0.0.1:5000/predict -d '{"text":"cats is bad, unrivaled in film history"}'`

Get the container ID

`docker ps`

Kill the container.

`docker kill <container id>`