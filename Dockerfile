FROM  ghcr.io/huggingface/text-generation-inference:latest

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD handler.py .

ENV model="tiiuae/falcon-7b-instruct"
ENV volume="/data"

ENTRYPOINT ["text-generation-launcher", "--model-id", "$model", "--volume", "$volume", "--gpu", "all","--shm-size", "1g"]