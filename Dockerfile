FROM python:3.12.3-alpine3.20
ENV PYTHONUNBUFFER 1

WORKDIR /app

COPY ./backend/requirements.txt ./
COPY ./backend/url_shortener/ ./

EXPOSE 8000


RUN python -m venv /venv && \
    /venv/bin/pip install -r requirements.txt

ENV PATH="/venv/bin:$PATH"

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]