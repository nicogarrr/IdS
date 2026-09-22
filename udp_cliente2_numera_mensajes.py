#!/usr/bin/env python3
"""Cliente UDP que numera cada datagrama enviado."""

import socket
import sys


def main() -> None:
    host = sys.argv[1] if len(sys.argv) > 1 else "localhost"
    puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    destino = (host, puerto)
    print(f"Enviando a {host}:{puerto} (escribe FIN para terminar)")

    n = 1
    while True:
        linea = input()
        if linea == "FIN":
            break
        mensaje = f"{n}: {linea}"
        s.sendto(mensaje.encode("utf-8"), destino)
        n += 1

    s.close()


if __name__ == "__main__":
    main()
