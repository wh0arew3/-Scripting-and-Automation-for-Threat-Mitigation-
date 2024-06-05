import nmap
import requests
import json
from datetime import datetime

def scan_ports(ip):
    scanner = nmap.PortScanner()
    scanner.scan(ip, '1-1024')  # Escanea los puertos del 1 al 1024
    open_ports = []
    for host in scanner.all_hosts():
        for proto in scanner[host].all_protocols():
            lport = scanner[host][proto].keys()
            for port in lport:
                if scanner[host][proto][port]['state'] == 'open':
                    open_ports.append(port)
    return open_ports

def check_vulnerabilities(port):

    vulns = {
        21: "FTP vulnerable a ataques de fuerza bruta",
        22: "SSH potencialmente vulnerable a ataques de diccionario",
        80: "HTTP podría tener vulnerabilidades XSS",
        443: "HTTPS podría tener configuraciones débiles de SSL/TLS"
    }
    return vulns.get(port, "No se encontraron vulnerabilidades conocidas")

def generate_report(ip, open_ports, vulnerabilities):
    report = {
        "timestamp": datetime.now().isoformat(),
        "ip_address": ip,
        "open_ports": open_ports,
        "vulnerabilities": vulnerabilities
    }
    with open('report.json', 'w') as report_file:
        json.dump(report, report_file, indent=4)
    print("Informe generado: report.json")

if __name__ == "__main__":
    target_ip = input("Ingresa la dirección IP a escanear: ")
    print(f"Escaneando puertos abiertos en {target_ip}...")
    open_ports = scan_ports(target_ip)
    print(f"Puertos abiertos encontrados: {open_ports}")

    vulnerabilities = {}
    for port in open_ports:
        vulnerabilities[port] = check_vulnerabilities(port)

    generate_report(target_ip, open_ports, vulnerabilities)
    print("Escaneo y verificación de vulnerabilidades completado.")
