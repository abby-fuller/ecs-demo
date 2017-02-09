FROM ubuntu:latest
MAINTAINER abbyfull@amazon.com
RUN apt-get update -y && apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python"]
CMD ["app.py"]
