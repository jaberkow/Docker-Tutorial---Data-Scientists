# Running a notebook out of a premade image and mounting data

Run a container from the [hugging face image](https://hub.docker.com/r/huggingface/transformers-pytorch-cpu), and mount the local data directory as a volume named "data" in the container's work directory.

`docker run -it -p 8888:8888 -v $PWD/data/:/workspace/data  huggingface/transformers-pytorch-cpu`

Start a jupyter notebook inside the container:

`jupyter notebook --ip 0.0.0.0 --no-browser --allow-root`

Copy and paste into your browswer one of the links that appears after 'Or copy and paste of these URLs:'

Now any changes you make to `/data` inside the container will be reflected on your host system, and vice versa.