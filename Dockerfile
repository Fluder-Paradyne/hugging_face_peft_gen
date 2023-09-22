from python:3.11.1-buster

WORKDIR /

COPY requirements.txt .
RUN pip install -r requirements.txt

ADD handler.py /handler.py
ADD app.py /app.py
ADD finetuned_model.py  /finetuned_model.py
ADD generation.py  /generation.py
ADD models.py /models.py

CMD [ "python", "-u", "/handler.py" ]