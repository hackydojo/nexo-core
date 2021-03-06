FROM tiangolo/uvicorn-gunicorn-fastapi:latest

COPY ./src /app
COPY ./requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV PORT 8080
