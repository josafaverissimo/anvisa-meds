FROM python:3.12-alpine3.19

COPY ../../api /api
COPY ../../scripts /scripts

WORKDIR /api

EXPOSE 8000

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install --upgrade  && \
    /venv/bin/pip install psycopg && \
    /venv/bin/pip install -r /api/requirements.txt && \
    adduser --disabled-password --no-create-home duser && \
    chown -R duser:duser /venv && \
    chmod -R +x /scripts

ENV PATH="/scripts:/venv/bin:$PATH"

USER duser

CMD ["commands.sh"]