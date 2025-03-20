import subprocess
import ipaddress

def ping_ip(host):
    comando = ["ping", "-c", "1", host] 
    resposta = subprocess.run(comando, capture_output=True, text=True)
    if resposta.returncode == 0:
        print(f'Conexão com {host} bem-sucedida!')
    else:
        print(f'Falha ao conectar com {host}.')

def verify(inicio_ip, fim_ip):
    # Converter os IPs de string para objetos ipaddress.IPv4Address
    inicio_ip = ipaddress.IPv4Address(inicio_ip)
    fim_ip = ipaddress.IPv4Address(fim_ip)

    # Iterar sobre os IPs no intervalo
    for ip_int in range(int(inicio_ip), int(fim_ip) + 1):
        ip = ipaddress.IPv4Address(ip_int)
        ping_ip(str(ip))

# Solicitar o intervalo de IPs
inicio_ip = input("Digite o primeiro IP: ")
fim_ip = input("Digite o último IP: ")

verify(inicio_ip, fim_ip)
