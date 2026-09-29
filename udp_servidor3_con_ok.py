import socket

PUERTO = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', PUERTO))
print(f"Servidor UDP escuchando en el puerto {PUERTO}...")

while True:
    datos, addr = s.recvfrom(1024)
    print(f"Peticion de {addr}: {datos.decode(errors='ignore')}")
    s.sendto(b"OK: " + datos, addr)
