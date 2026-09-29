import socket

PUERTO = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', PUERTO))
print(f"Servidor broadcast escuchando en el puerto {PUERTO}...")

while True:
    datos, addr = s.recvfrom(1024)
    print(f"Descubierto por {addr[0]}:{addr[1]} -> Mensaje: {datos.decode(errors='ignore')}")
    s.sendto(b"DISPONIBLE", addr)
