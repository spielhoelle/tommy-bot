FROM python:3.8.12
WORKDIR /app
COPY . .
RUN apt update && apt upgrade -y && apt install -y python3 python3-pip  
RUN pip3 install --default-timeout=100 -r requirements.txt
RUN ls -la
RUN pwd
EXPOSE 5000
CMD python3 app.py
 