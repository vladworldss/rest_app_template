FROM python:3.10.0 AS base

# ставим боевые зависимости
COPY ./poetry.lock ./pyproject.toml /usr/src/app/
WORKDIR /usr/src/app/
RUN apt-get install gcc
RUN python -m pip install poetry
RUN python -m poetry install --no-root --no-interaction
CMD poetry run python main.py
