FROM python:3.6-slim-buster
COPY . /app
WORKDIR /app
RUN pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip3 install -r requirements.txt
RUN python preload.py
CMD ["python3","app.py"]