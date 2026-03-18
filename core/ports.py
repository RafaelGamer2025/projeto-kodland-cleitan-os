import socket

def scan_ports(host, log):
    portas = [21, 22, 80, 443, 3306, 8080]

    log(f"\n[PORT SCAN] {host}")

    for p in portas:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((host, p))
            log(f"[ABERTA] {p}")
            s.close()
        except:
            log(f"[FECHADA] {p}")