FROM python:latest

RUN mkdir /ibama

COPY requirements.txt /ibama

WORKDIR /ibama

RUN pip install -r requirements.txt

COPY . /ibama

CMD ["python", "scraping.py"]