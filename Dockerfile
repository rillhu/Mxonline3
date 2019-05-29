FROM python:3.6

WORKDIR /app

COPY requirements.txt .
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

ADD . /app

CMD ["python","manage.py","runserver","0.0.0.0:8000"]