FROM ubuntu:22.04
WORKDIR /app
COPY . .
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN python3 -m pip install -r requirements.txt
# RUN echo "SERV_ID=$(bash -c 'echo \""$RANDOM"\"')" >> .env
EXPOSE 5000
CMD ["python3", "server.py"]