FROM python:3.11
WORKDIR /project_bill
COPY requirements.txt /project_bill
RUN pip3 install -r /project_bill/requirements.txt
COPY . /web
CMD gunicorn project_bill.wsgi:application --bind 0.0.0.0:8000