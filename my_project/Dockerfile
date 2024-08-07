FROM python:3.11

WORKDIR /my_project

COPY requirment.txt .

RUN pip install --no-cache-dir -r requirment.txt 

RUN apt-get install libmariadb-dev-compat libmariadb-dev

RUN pip install wheel

RUN pip install mysqlclient

COPY . .

EXPOSE 8000

CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]