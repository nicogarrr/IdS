"""Servidor UDP sencillo: imprime cada datagrama y su origen."""

import socket
import sys


def main() -> None:
    puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", puerto))
    print(f"Servidor UDP escuchando en puerto {puerto}")

    while True:
        datagrama, origen = s.recvfrom(1024)
        texto = datagrama.decode("utf-8")
        print(f"Desde {origen}: {texto}")


if __name__ == "__main__":
    main()
