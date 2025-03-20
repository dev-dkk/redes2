import socket

def verificar_porta(ip, porta):
    # Criar um socket para a conexão
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Definir o tempo de espera (timeout) em segundos
    sock.settimeout(5)
    
    try:
        # Tentar se conectar ao servidor na porta especificada
        sock.connect((ip, porta))
    except socket.error:
        # Se não conseguir conectar, a porta está fechada
        return False
    else:
        # Se a conexão for bem-sucedida, a porta está aberta
        return True
    finally:
        # Fechar o socket
        sock.close()

# Solicitar o IP e a porta ao usuário
ip = input("Digite o IP do servidor: ")
porta = int(input("Digite o número da porta a ser verificada: "))

# Verificar se a porta está aberta ou fechada
if verificar_porta(ip, porta):
    print(f"A porta {porta} está aberta no servidor {ip}.")
else:
    print(f"A porta {porta} está fechada no servidor {ip}.")
