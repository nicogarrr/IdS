import sys, socket

bcast_ip = sys.argv[1] if len(sys.argv) > 1 else '172.18.255.255'
port = int(sys.argv[2]) if len(sys.argv) > 2 else 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.settimeout(2.0)

print(f"Enviando mensaje de broadcast a {bcast_ip}:{port}...")
s.sendto(b"HOLA_BROADCAST", (bcast_ip, port))

servidores = []
while True:
    try:
        resp, addr = s.recvfrom(1024)
        print(f"Respuesta recibida del servidor {addr}: {resp.decode(errors='ignore')}")
        servidores.append(addr)
    except socket.timeout:
        break

if servidores:
    primer_servidor = servidores[0]
    print(f"\nSeleccionado primer servidor: {primer_servidor}")
    s.sendto(b"PETICION_FINAL", primer_servidor)
else:
    print("No se recibieron respuestas de servidores.")
