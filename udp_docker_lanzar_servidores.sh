#!/bin/bash
docker network create pruebas 2>/dev/null || true
docker run -d --name srv_bcast1 --network pruebas -v $(pwd):/app python:3.7 python -u /app/udp_servidor6_broadcast.py
docker run -d --name srv_bcast2 --network pruebas -v $(pwd):/app python:3.7 python -u /app/udp_servidor6_broadcast.py
docker run -d --name srv_bcast3 --network pruebas -v $(pwd):/app python:3.7 python -u /app/udp_servidor6_broadcast.py
docker ps
