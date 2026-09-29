#!/bin/bash
docker run -it --rm --network pruebas --name cliente_bcast -v $(pwd):/app python:3.7 python /app/udp_cliente6_broadcast.py 172.18.255.255 9999
