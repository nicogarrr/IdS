"""Cliente UDP: envía líneas de teclado hasta FIN."""

import socket
import sys


def main() -> None:
    host = sys.argv[1] if len(sys.argv) > 1 else "localhost"
    puerto = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    destino = (host, puerto)
    print(f"Enviando a {host}:{puerto} (escribe FIN para terminar)")

    while True:
        linea = input()
        if linea == "FIN":
            break
        s.sendto(linea.encode("utf-8"), destino)

    s.close()


if __name__ == "__main__":
    main()
