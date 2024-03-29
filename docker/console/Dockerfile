ARG ALPINE_VERSION=3.18
ARG PYTHON_VERSION=3.12
ARG NODE_VERSION=21

FROM ${ARCH}python:${PYTHON_VERSION}-alpine${ALPINE_VERSION} AS python

ARG DOCKER_GID=130
# ENV MKP224O_TAG=v1.5.0

ENV FLASK_WPA_SOCKET_PATH=/var/run/sockets/wpa_supplicant \
    FLASK_NDS_SOCKET_PATH=/var/run/sockets/nds \
    FLASK_DOCKER_SOCKET_PATH=/var/run/sockets/docker.sock \
    FLASK_LOG_LEVEL=DEBUG \
    FLASK_DEBUG=true \
    FLASK_HOST=0.0.0.0 \
    FLASK_PORT=8008 \
    FLASK_DB_PATH=/var/lib/console/db.sqlite3 \
    FLASK_CACHE_TYPE=flask_caching.contrib.uwsgicache.UWSGICache \
    FLASK_SHANTY_BASE_URL=https://www.homeland-social.com/ \
    SSH_KEY_FILE= \
    SSH_HOST_KEYS_FILE=

# Add the python application, be sure to exclude dotfiles.
ADD ./back/api /app/api/
ADD ./back/Pipfile* /app/
ADD ./docker/console/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Install Python
WORKDIR /app
RUN apk add --no-cache py3-pip git build-base py3-cryptography python3-dev \
                       libsodium libsodium-dev autoconf libffi libffi-dev \
                       musl-dev pcre2 pcre2-dev openssl openssl-dev binutils \
                       sqlite-libs rust cargo
# RUN apk add --no-cache linux-headers build-base python3 py3-pip py3-cryptography mailcap \
#                        python3-dev git libsodium libsodium-dev autoconf libffi libffi-dev \
#                        musl-dev pcre2 pcre2-dev openssl openssl-dev
RUN pip install -U pip
RUN pip install pipenv
RUN pipenv install --system --skip-lock
# RUN mkdir -p /usr/local/src && cd /usr/local/src
# RUN git clone --branch ${MKP224O_TAG} https://github.com/cathugger/mkp224o.git && cd mkp224o
# RUN ./autogen.sh && ./configure --enable-regex=yes
# RUN make && install mkp224o /usr/local/bin/mkp224o
RUN addgroup -g ${DOCKER_GID} docker
RUN adduser nobody docker

ENTRYPOINT [ "/entrypoint.sh" ]


FROM python as strip

#RUN find /usr/local -name '*.so' | xargs strip -s
RUN pip uninstall -y pipenv
RUN pip uninstall -y pip
RUN rm -rf /usr/local/lib/python*/ensurepip
RUN rm -rf /usr/local/lib/python*/idlelib
RUN rm -rf /usr/local/lib/python*/distutils/command
RUN rm -rf /usr/local/lib/python*/lib2to2
RUN rm -rf /usr/local/lib/python*/__pycache__/*
RUN find /usr/local/include/python* -not -name pyconfig.h -type f -exec rm {} \;
RUN find /usr/local/bin \( -not -name 'python*' -and -not -name 'uwsgi' \) -and \( -type f -o -type l \) -exec rm {} \;
RUN rm -rf /usr/local/share/*


FROM node:${NODE_VERSION}-alpine${ALPINE_VERSION} AS node

ADD ./front /front

WORKDIR /front
ENV NODE_OPTIONS=--openssl-legacy-provider
RUN npm i
RUN npm run build

ENTRYPOINT [ "npm", "run", "serve" ]


FROM ${ARCH}alpine:${ALPINE_VERSION} AS final

RUN apk add --no-cache openssl zlib libsodium libffi libexpat \
                       sqlite-libs docker-cli docker-cli-compose

COPY --from=strip /app/api /app/api
COPY --from=strip /usr/local/ /usr/local/
COPY --from=strip /entrypoint.sh /entrypoint.sh
COPY --from=node /front/dist /app/assets
ADD ./docker/console/docker-compose.yml /app

WORKDIR /app

ENTRYPOINT [ "/entrypoint.sh" ]
