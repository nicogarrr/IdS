#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cliente UDP mejorado: id aleatorio, ACK comprobado, connect()+recv()."""

import random
import socket
import sys

import salida_utf8


def main() -> None:
    salida_utf8.configurar()
    host = sys.argv[1] if len(sys.argv) > 1 else "localhost"
    puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # En UDP, connect() filtra datagramas a la IP:puerto del servidor
    s.connect((host, puerto))
    print(f"Enviando a {host}:{puerto} (escribe FIN para terminar)")

    while True:
        linea = input()
        if linea == "FIN":
            break

        msg_id = str(random.randint(1, 1_000_000_000))
        payload = f"{msg_id}|{linea}".encode("utf-8")
        timeout = 0.1

        while True:
            s.send(payload)
            s.settimeout(timeout)
            try:
                datagrama = s.recv(1024).decode("utf-8")
                if datagrama == f"OK|{msg_id}":
                    print(f"Recibida confirmación de {msg_id}")
                    break
                else:
                    print(f"Recibido datagrama no esperado: {datagrama}")
            except (socket.timeout, ConnectionResetError):
                print("ERROR. El datagrama de confirmación no llega")
                timeout *= 2
                if timeout > 2:
                    print("Puede que el servidor esté caído. Inténtelo más tarde")
                    s.close()
                    return
            except Exception:
                raise

    s.close()


if __name__ == "__main__":
    main()
