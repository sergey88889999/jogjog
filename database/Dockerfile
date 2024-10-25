FROM mysql:8.0-bookworm

COPY ./init.sql /docker-entrypoint-initdb.d/

HEALTHCHECK --interval=10s --timeout=5s --start-period=30s --retries=3 \
  CMD mysqladmin ping -h localhost -u root --password="${MYSQL_ROOT_PASSWORD}"
