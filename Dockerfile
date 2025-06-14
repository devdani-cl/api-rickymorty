FROM python:3.10

WORKDIR /app

ENTRYPOINT ["python"]

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["opcional.py"]