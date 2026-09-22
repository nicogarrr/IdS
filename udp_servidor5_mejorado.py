#!/usr/bin/env python3
"""Servidor UDP mejorado: ACK con id, deduplicación y simulación de pérdidas."""

import random
import socket
import sys


def main() -> None:
    puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 9999

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", puerto))
    print(f"Servidor UDP mejorado escuchando en puerto {puerto}")

    vistos = set()

    while True:
        datagrama, origen = s.recvfrom(1024)
        if random.randint(0, 1) == 0:
            print("Simulando paquete perdido")
            continue

        texto = datagrama.decode("utf-8")
        # Formato esperado: "id|contenido"
        partes = texto.split("|", 1)
        if len(partes) != 2:
            print(f"Desde {origen}: datagrama mal formado: {texto}")
            continue

        msg_id, contenido = partes
        ack = f"OK|{msg_id}".encode("utf-8")

        if msg_id in vistos:
            # Duplicado: solo reenviar ACK, sin repetir la acción
            print(f"Duplicado {msg_id} desde {origen}; reenviando ACK")
            s.sendto(ack, origen)
            continue

        vistos.add(msg_id)
        print(f"Desde {origen}: [{msg_id}] {contenido}")
        s.sendto(ack, origen)


if __name__ == "__main__":
    main()
