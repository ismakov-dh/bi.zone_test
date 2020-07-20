FROM python:3.8-alpine

WORKDIR /opt/test_app/

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./ ./

CMD [ "python3", "app.py"]