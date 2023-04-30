FROM python:3.11-bullseye

ENV YOUR_ENV=${YOUR_ENV} \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 

RUN pip install poetry

WORKDIR /code/

COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY /src/ .

ENTRYPOINT ["poetry", "run", "uvicorn", "app.main:app"]