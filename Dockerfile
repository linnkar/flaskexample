FROM python:2.7-alpine3.8
RUN adduser -D flask

WORKDIR /home/flask
COPY boot.sh boot.sh
COPY randint.py randint.py
COPY templates/randint.html templates/randint.html
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
#RUN chmod +x boot.sh

#RUN bin/sh
#ENV FLASK_APP randint.py
RUN chown -R flask:flask .
USER flask

EXPOSE 5002
ENTRYPOINT ./boot.sh


