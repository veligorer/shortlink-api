from python:3.7

RUN apt-get update && apt-get install -y python3-tk

RUN mkdir /app/
WORKDIR /app/

COPY ./app/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000

COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
