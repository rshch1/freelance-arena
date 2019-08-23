
FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /freelance

WORKDIR /freelance

ADD . /freelance/
RUN  apt-get update && apt-get install -y postgresql
RUN pip install -r ./requirements/local.txt
EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["migrate", "runserver", "0.0.0.0:8000"]