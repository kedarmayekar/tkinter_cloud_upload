FROM python:3.8
COPY . /app
WORKDIR /app
RUN apt-get update && apt-get install -y python3-tk
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]
