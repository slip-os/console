FROM ${ARCH}alpine:3.18

ADD ./docker/conduit/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENV SSH_KEY_PATH=/etc/ssh/keys/id_ecdsa
ENV SSH_KEY_TYPE=ecdsa

RUN apk add --no-cache jq curl dropbear dropbear-ssh

ENTRYPOINT [ "/entrypoint.sh" ]
