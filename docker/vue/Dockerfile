FROM node:21.7.1-alpine3.19

COPY ./vue-app /vue-app
COPY ./docker/vue/scripts /scripts

WORKDIR /vue-app

EXPOSE 9090

RUN adduser --disabled-password --no-create-home duser && \
    chown -R duser:duser /vue-app && \
    chmod -R +x /scripts && \
    chmod -R u=rw,g=rw,o=rw /vue-app

ENV PATH="/scripts:$PATH"

CMD ["commands.sh"]