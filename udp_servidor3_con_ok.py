#!/usr/bin/env python3
"""Servidor UDP con simulación de pérdidas y ACK 'OK'."""

import random
import socket
import sys


def main() -> None:
    puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", puerto))
    print(f"Servidor UDP escuchando en puerto {puerto}")

    while True:
        datagrama, origen = s.recvfrom(1024)
        if random.randint(0, 1) == 0:
            print("Simulando paquete perdido")
        else:
            texto = datagrama.decode("utf-8")
            print(f"Desde {origen}: {texto}")
            s.sendto(b"OK", origen)


if __name__ == "__main__":
    main()
