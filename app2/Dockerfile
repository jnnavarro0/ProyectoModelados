# syntax=docker/dockerfile:1

FROM python:3.7-alpine

RUN mkdir /app2
WORKDIR /app2
COPY . /app2

RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["nodemon", "--watch", ".", "--ext", "py", "--exec", "flask", "run", "--host=0.0.0.0"]