import requests
import socket
import sys


def check_internet_connectivity():
    try:
        requests.get('http://www.google.com', timeout=5)
        return True
    except requests.ConnectionError as e:
        print(f"Sua conexão foi perdida: {e}")
        print("Confira algumas dicas de como corrigir": ")
        print("Verifique com o seu provedor de internet se você está sofrendo com problemas de roteamento, isso é muito comum em provedores que usam conexão primitiva.")
        print(
            "- Verifique se as configurações de seu roteador estão corretamente ajustadas.")
        return False
    except socket.timeout as e:
        print(f"Conexão interrompida: {e}")
        print("seguem algumas formas de corrigir:")
        print("- Verifique a velocidade de sua conexão, espero que sua internet não seja uma tortuguita.")
        print("- Verifique se o servidor do site não está apresentando algum problema.")
        return False
    except requests.ConnectTimeout as e:
        print(f"Conexão interrompida: {e}")
        print("Possíveis correções:")
        print("- Verifique a velocidade de sua conexão, novamente eu digo, a internet precisa ser veloz para ser usável.")
        print("- Verifique se o servidor do site não está apresentando alguma instabilidade ou indisponibilidade temporária.")
        print("- Verifique se as portas de seu roteador e firewall estão corretamente ajustadas.")
        return False
    except requests.ReadTimeout as e:
        print(f"Conexão perdida: {e}")
        print("Algumas formas de correção incluem:")
        print("- Verifique a sua conexão com a internet, vale a pena verificar se todos os cabos estão conectados e se há sinal de internet.")
        print("- Verifique se o servidor do site não apresenta problemas momentâneos.")
        print("- Verifique se o firewall de seu computador, ou mesmo da rede não está impedindo a conexão.")
        return False


if check_internet_connectivity():
    print("Você está conectado à internet.")
    sys.exit(0)  # Código de saída 0 indica que tudo está normal
else:
    print("A internet não está conectada.")
    sys.exit(1)  # Situação de saída 1 indica uma falha
