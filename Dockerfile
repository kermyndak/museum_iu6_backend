FROM python:3.9


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r /code/requirements.txt


# COPY ./app /code/app


# CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "80", "--workers", "4"]

EXPOSE 8000
