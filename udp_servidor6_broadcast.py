#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Servidor UDP del protocolo HOLA (descubrimiento por broadcast)."""

import socket
import sys

import salida_utf8

PUERTO = 12345


def main() -> None:
    salida_utf8.configurar()
    puerto = int(sys.argv[1]) if len(sys.argv) > 1 else PUERTO

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind(("", puerto))
    print(f"Servidor HOLA escuchando en puerto {puerto} (modo broadcast)")

    while True:
        datagrama, origen = s.recvfrom(1024)
        texto = datagrama.decode("utf-8").strip()
        ip_cliente = origen[0]

        if texto == "BUSCANDO HOLA":
            print(f"Descubrimiento desde {origen}")
            s.sendto("IMPLEMENTO HOLA".encode("utf-8"), origen)
        elif texto == "HOLA":
            respuesta = f"HOLA: {ip_cliente}"
            print(f"Servicio HOLA para {origen} -> {respuesta}")
            s.sendto(respuesta.encode("utf-8"), origen)
        else:
            print(f"Datagrama ignorado desde {origen}: {texto}")


if __name__ == "__main__":
    main()
