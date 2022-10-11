FROM python:3.8
ENV PYTHONBUFFERED=1
RUN ls
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY ./jango-assessment /app
WORKDIR /app
EXPOSE 8000
EXPOSE 5432
# CMD ["python", "manage.py", "runserver", "-h", "0.0.0.0"]