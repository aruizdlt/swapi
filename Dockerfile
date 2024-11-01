FROM python:3.11-slim
WORKDIR /srv
COPY requirements.txt /srv/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /srv/requirements.txt
COPY ./app /srv/app/
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0","--port 8000"]