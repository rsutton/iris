FROM python:3.7

ADD iris /app/iris
COPY requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000
ENTRYPOINT ["python"]
CMD ["iris/app.py"]