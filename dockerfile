FROM ubuntu:latest
MAINTAINER Sam Ortiz "samuelortizibarra@gmail.com
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip build-essential

COPY . /app

WORKDIR /app/
RUN chmod 644 app.py
RUN ls
RUN pip3 freeze > requirements.txt
RUN pip3 install -r req.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]


