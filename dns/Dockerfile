FROM ubuntu:24.04

# Install PowerDNS, MySQL backend, and gettext-base for envsubst
RUN apt-get update && apt-get install -y \
    pdns-server \
    pdns-backend-mysql \
    gettext-base \
    && rm -rf /var/lib/apt/lists/*

# Remove default config
RUN rm -f /etc/powerdns/pdns.d/bind.conf

# Copy template config
COPY pdns.conf.template /etc/powerdns/pdns.d/gmysql.conf.template

# Create entrypoint script
RUN echo '#!/bin/bash\n\
envsubst < /etc/powerdns/pdns.d/gmysql.conf.template > /etc/powerdns/pdns.d/gmysql.conf\n\
exec /usr/sbin/pdns_server\n\
' > /entrypoint.sh && chmod +x /entrypoint.sh

EXPOSE 53/tcp
EXPOSE 53/udp

CMD ["/entrypoint.sh"]