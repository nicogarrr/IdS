#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cliente UDP numerado que espera confirmación OK con timeout."""

import socket
import sys

import salida_utf8


def main() -> None:
    salida_utf8.configurar()
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

        s.settimeout(0.1)
        try:
            datagrama, origen = s.recvfrom(1024)
            datagrama = datagrama.decode("utf-8")
            if datagrama == "OK":
                print("Recibida confirmación")
            else:
                print("Recibido datagrama no esperado")
        except socket.timeout:
            print("ERROR. El datagrama de confirmación no llega")
        except Exception:
            raise

        n += 1

    s.close()


if __name__ == "__main__":
    main()
