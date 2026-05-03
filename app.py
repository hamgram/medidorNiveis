# IMPORTAÇÃO DAS BIBLIOTECAS
import random
from colorama import Fore, Style

# LISTA DOS NÍVEIS DE ÁGUA
niveisReservatorio = ["Muito baixo (crítico)","Baixo","Médio","Alto","Muito Alto (alerta)"]

# ENTRADA: VARIÁVEL QUE DEFINE O NÍVEL DE ÁGUA ALEATÓRIAMENTE 
nivelAtual = random.randint(0,4)

# PROCESSAMENTO: FUNÇÃO PARA DEFINIR A COR DA MENSAGEM. RECEBE O NÍVEL DE ÁGUA E RETORNA A COR.
def selecionarCor(nivelAgua):
    match nivelAgua:
        case 0:
            return Fore.RED
        case 1:
            return Fore.YELLOW
        case 2:
            return Fore.GREEN
        case 3:
            return Fore.CYAN
        case 4:
            return Fore.BLUE

# VARIÁVEL PARA ARMAZENAR A COR DEFINIDA 
corEscolhida = selecionarCor(nivelAtual)

# VAIÁVEL PARA ARMAZENAR O NÍVEL DO RESERVATÓIO 
nivelIndicado = niveisReservatorio[nivelAtual]

# SAÍDA: IMPRESSÃO  DA MENSAGEM E RESET DAS CONFIGURAÇÕES
print(f"{corEscolhida}O nível do reservatório de água é {nivelIndicado.upper()}.{Style.RESET_ALL}")


