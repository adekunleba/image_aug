FROM amd64/python:3.9.4-alpine AS app
LABEL maintainer="Adekunle Babatunde <adekunleba@gmail.com>"

WORKDIR /app

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN apk update \
  &&  apk add python3-dev gcc libc-dev libffi-dev build-base alpine-sdk openssl-dev jpeg-dev zlib-dev \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && addgroup -S python && adduser -S python -G python \
  && chown python:python -R /app

USER python

COPY --chown=python:python requirements*.txt ./

RUN pip install -r ./requirements.txt


COPY --chown=python:python bin/ ./bin
COPY --chown=python:python ./app ./app

RUN chmod 0755 bin/*
RUN chmod +x bin/docker-entrypoint.sh



RUN ls -lh

ARG PORT="8000"
ENV PORT=${PORT}

ARG FLASK_ENV="production"
ENV FLASK_ENV="${FLASK_ENV}" \
    FLASK_APP="app" \
    FLASK_SKIP_DOTENV="true" \
    PYTHONPATH="." \
    PATH="${PATH}:/home/python/.local/bin" \
    USER="python"

ENTRYPOINT [ "bin/docker-entrypoint.sh" ]

EXPOSE ${PORT}
# gunicorn -c bin/gunicorn.conf.py "app:create_app()"
CMD ["gunicorn", "-c", "bin/gunicorn.conf.py", "app:app"]
