FROM python:3.8.5
FROM ubuntu:18.04


WORKDIR /usr/src/app

COPY Download_And_Tweet.py .
COPY TelegramKeys.py .
COPY keys.py .
#i think its unnessery

RUN mkdir media

COPY requirements.txt .

RUN apt-get update && apt-get install -y apt-transport-https
RUN set -xe \
    && apt-get update \
    &&  apt -y install python3-pip

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install telethon==1.17.5
RUN pip3 install asyncio==3.4.3


CMD [ "python3" ,"Download_And_Tweet.py"]