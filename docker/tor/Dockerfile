FROM ${ARCH}alpine:3.15

RUN apk add --no-cache curl && \
    apk add --no-cache --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing/ tor && \
    sed "1s/^/SocksPort 0.0.0.0:9050\n/" /etc/tor/torrc.sample > /etc/tor/torrc

EXPOSE 9050

HEALTHCHECK --interval=60s --timeout=15s --start-period=20s \
    CMD curl -s --socks5 127.0.0.1:9050 'https://check.torproject.org/' | grep -qm1 Congratulations

VOLUME ["/var/lib/tor"]

USER tor

CMD ["tor"]
