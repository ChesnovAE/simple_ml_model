FROM python:3.8-slim

WORKDIR /application

COPY ./requirements.txt /application/
RUN pip3 install -r requirements.txt

COPY  ./app.py /application/
COPY ./models /application/models
COPY ./utils /application/utils
COPY ./configds /application/configs

ENTRYPOINT [ "python3", "app.py" ]