FROM python:3.7

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY main.py /app/

ENTRYPOINT [ "python3", "/app/main.py" ]