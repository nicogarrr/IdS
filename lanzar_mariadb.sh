#!/bin/bash
docker stop mariadb 2>/dev/null || true
docker run --name mariadb \
    -e MYSQL_ROOT_PASSWORD=claveroot \
    -v $(pwd)/basedatos:/var/lib/mysql \
    --network pruebas \
    --rm -d mariadb
docker ps --filter name=mariadb
