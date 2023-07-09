FROM python:3

ADD myScript.py /

RUN pip install pystrich

CMD [ "python", "./myScript.py" ]
