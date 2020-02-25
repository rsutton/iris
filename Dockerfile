FROM python:3.7

ADD iris /app
COPY requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000
ENTRYPOINT ["python"]
CMD ["app.py"]