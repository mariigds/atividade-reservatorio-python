import colorama
from colorama import Fore, Style

# Inicializa o colorama (necessário especialmente para Windows)
colorama.init()

def exibir_status_reservatorio(nivel):
    """
    Função responsável por definir a cor e exibir a mensagem 
    conforme o nível informado.
    """
    
    # Lista de situações (Índice 0 corresponde ao Nível 1, e assim por diante)
    situacoes = [
        "Muito baixo (crítico)", # Nível 1
        "Baixo",                 # Nível 2
        "Médio",                 # Nível 3
        "Alto",                  # Nível 4
        "Muito alto (alerta)"    # Nível 5
    ]

    # Mapeamento de cores baseado no nível
    if nivel == 1:
        cor = Fore.RED
    elif nivel == 2:
        cor = Fore.YELLOW
    elif nivel == 3:
        cor = Fore.GREEN
    elif nivel == 4:
        cor = Fore.CYAN
    elif nivel == 5:
        cor = Fore.BLUE
    else:
        print("Nível inválido!")
        return

    # Exibição da mensagem com a cor correspondente
    # O índice da lista é sempre nível - 1
    mensagem = situacoes[nivel - 1]
    print(f"Status do Reservatório [Nível {nivel}]: {cor}{mensagem}{Style.RESET_ALL}")

# --- Simulação do Ambiente Real ---
def simular_sistema():
    print("=== SISTEMA DE MONITORAMENTO HIDRÁULICO ===\n")
    
    # Simulando a leitura de diferentes níveis
    niveis_para_testar = [1, 2, 3, 4, 5]
    
    for n in niveis_para_testar:
        exibir_status_reservatorio(n)

if __name__ == "__main__":
    simular_sistema()
    