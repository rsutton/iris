FROM python:3.7

ADD static /app/static/
ADD templates /app/templates/
COPY app.py /app
COPY requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000
ENTRYPOINT ["python"]
CMD ["app.py"]