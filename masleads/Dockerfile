FROM python:3.10 AS api

ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.6.1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN apt-get update \
    && pip install "poetry==${POETRY_VERSION}"

WORKDIR /masleads/
COPY . /masleads/
RUN poetry install

ENTRYPOINT python main.py
