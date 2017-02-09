FROM ubuntu:latest
MAINTAINER abbyfull@amazon.com
RUN apt-get update -y && apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]

EXPOSE 3000

CMD ["app.py"]
