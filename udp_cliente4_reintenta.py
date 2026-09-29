import sys, socket

host = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
port = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(2.0)
msg = b"Hola servidor UDP"

for intento in range(1, 4):
    try:
        print(f"Enviando intento {intento} a {host}:{port}...")
        s.sendto(msg, (host, port))
        resp, addr = s.recvfrom(1024)
        print(f"Respuesta de {addr}: {resp.decode(errors='ignore')}")
        break
    except socket.timeout:
        print("Timeout alcanzado, reintentando...")
