FROM  ghcr.io/huggingface/text-generation-inference:latest

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD handler.py .

ENV model="tiiuae/falcon-7b-instruct"
ENV volume="/data"
ENV trust_remote_code=True
ENV DISABLE_CUSTOM_KERNELS=true

CMD [ "--model-id", "tiiuae/falcon-7b-instruct"]
# CMD [ "python3", "-u", "/handler.py" ]