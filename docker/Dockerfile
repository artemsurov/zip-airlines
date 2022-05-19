FROM python:3.9-buster

WORKDIR /app

ENV POETRY_HOME=/bin/poetry
ENV PATH="${POETRY_HOME}/bin/:${PATH}"

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN echo "deb http://apt.postgresql.org/pub/repos/apt buster-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN apt-get update
RUN apt-get -y install postgresql-client-12 tidy libxml2-utils jing vim libyajl2

COPY ["pyproject.toml", "poetry.lock", "/app/"]
RUN poetry config virtualenvs.create false --local
RUN poetry install -n
