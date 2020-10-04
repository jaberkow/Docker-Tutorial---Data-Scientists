FROM huggingface/transformers-pytorch-cpu
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN python3 preload.py
CMD ["python3","app.py"]