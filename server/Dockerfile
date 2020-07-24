FROM python:3

WORKDIR /server

COPY . .

RUN pip3 install -r ./server/requirements.txt

CMD [ "python3", "server.py" ]