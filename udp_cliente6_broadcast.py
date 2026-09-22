#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cliente UDP del protocolo HOLA (descubrimiento por broadcast)."""

import socket
import sys

import salida_utf8

PUERTO = 12345
TIMEOUT_DESCUBRIMIENTO = 1.0


def ip_local() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


def direccion_broadcast(ip: str) -> str:
    # En el laboratorio la máscara suele ser /24 → x.y.z.255
    partes = ip.split(".")
    if len(partes) == 4:
        return ".".join(partes[:3] + ["255"])
    return "255.255.255.255"


def main() -> None:
    salida_utf8.configurar()
    puerto = PUERTO
    if len(sys.argv) > 1:
        bcast = sys.argv[1]
    else:
        bcast = direccion_broadcast(ip_local())
    if len(sys.argv) > 2:
        puerto = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    print(f"Buscando servidores HOLA por broadcast a {bcast}:{puerto}")
    s.sendto("BUSCANDO HOLA".encode("utf-8"), (bcast, puerto))

    servidores = []
    primer_servidor = None
    s.settimeout(TIMEOUT_DESCUBRIMIENTO)

    while True:
        try:
            datagrama, origen = s.recvfrom(1024)
            texto = datagrama.decode("utf-8")
            if texto == "IMPLEMENTO HOLA":
                ip_servidor = origen[0]
                print(f"Servidor encontrado: {ip_servidor}")
                servidores.append(ip_servidor)
                if primer_servidor is None:
                    primer_servidor = ip_servidor
        except socket.timeout:
            break

    if primer_servidor is None:
        print("No se ha encontrado ningún servidor HOLA")
        s.close()
        return

    print(f"Probando el servicio con {primer_servidor}")
    s.settimeout(None)
    s.sendto("HOLA".encode("utf-8"), (primer_servidor, puerto))
    respuesta, origen = s.recvfrom(1024)
    print(f"Respuesta de {origen[0]}: {respuesta.decode('utf-8')}")
    s.close()


if __name__ == "__main__":
    main()
