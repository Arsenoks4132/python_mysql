FROM python:3.12

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY scripts/ scripts/

RUN touch my_test.log

CMD python scripts/hello.py "Hello from python!" && tail -F my_test.log
