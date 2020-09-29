FROM python:3.8.6-slim

WORKDIR "/data/www"

COPY ./ /data/www

RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ && mkdir logs 

CMD [ "-c", "gunicorn.py", "main:app" ]
ENTRYPOINT [ "gunicorn" ]
