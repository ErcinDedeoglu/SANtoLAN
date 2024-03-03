FROM python:3.8-slim

WORKDIR /src

COPY src/ .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=api.py

CMD ["flask", "run", "--host=0.0.0.0"]
