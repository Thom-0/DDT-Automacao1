import pyautogui
import time

# Caminho base das imagens (Trial 4)
caminho_base = r"C:\Users\Renlorck\Documents\DDT-Automacaoo\imagens\Trial_4"

# Função para procurar e clicar em uma imagem
def procurar_e_clicar(imagem, caminho_base, tempo_espera=1):
    caminho_completo = f"{caminho_base}\\{imagem}"
    print(f"Procurando: {caminho_completo}")

    botao = pyautogui.locateOnScreen(caminho_completo, confidence=0.7)

    if botao is not None:
        centro = pyautogui.center(botao)
        pyautogui.click(centro)
        print(f"Imagem encontrada e clicada: {imagem}")
    else:
        print(f"Imagem NÃO encontrada: {imagem}")

    time.sleep(tempo_espera)

# Função de batalha
def executar_batalha():
    batalha = None
    while batalha is None:
        try:
            batalha = pyautogui.locateOnScreen(f"{caminho_base}\\batalha_iniciada.png", confidence=0.7)
        except pyautogui.ImageNotFoundException:
            print("Imagem de batalha não encontrada.")
            time.sleep(1)

    Seta_de_batalha = None
    while Seta_de_batalha is None:
        try:
            Seta_de_batalha = pyautogui.locateOnScreen(f"{caminho_base}\\Seta_de_batalha.png", confidence=0.7)
            if Seta_de_batalha is not None:
                pyautogui.click(Seta_de_batalha)
                print("Seta de batalha encontrada e clicada.")
            time.sleep(1)
        except pyautogui.ImageNotFoundException:
            print("Imagem da Seta de Batalha não encontrada.")
            time.sleep(1)

    while batalha is not None:
        sua_vez = None
        while sua_vez is None:
            try:
                sua_vez = pyautogui.locateOnScreen(f"{caminho_base}\\sua_vez.png", confidence=0.7)
                if sua_vez is not None:
                    teclas_numero = ['num1', 'num2', 'num4']
                    for tecla in teclas_numero:
                        pyautogui.press(tecla)
                        time.sleep(0.05)
                    print("Teclas pressionadas para 'Sua vez'.")

                    pyautogui.keyDown("space")
                    time.sleep(2.5)
                    pyautogui.keyUp("space")
                    time.sleep(1)
            except pyautogui.ImageNotFoundException:
                print("Imagem 'Sua vez' não encontrada.")
                pass

            fim_do_jogo = None
            try:
                fim_do_jogo = pyautogui.locateOnScreen(f"{caminho_base}\\fim_do_Jogo.png", confidence=0.7)
                if fim_do_jogo:
                    print("Fim do jogo detectado.")
                    time.sleep(20)
                    break
            except pyautogui.ImageNotFoundException:
                print("Imagem 'Fim do Jogo' não encontrada, tentando novamente...")
                time.sleep(5)

        if fim_do_jogo:
            print("Aguardando nova batalha...")
            time.sleep(3)
            start_2_func()

# Lista de imagens para o start 1
start_1 = [
    "select_instancia.png",
    "ins_unica.png",
    "ins_trial4.png",
    "modo_heroi.png",
    "sim.png",
    "aSinicio.png"
]

# Lista de imagens para o start 2
start_2 = [
    "select_instancia.png",
    "ins_trial4.png",
    "modo_heroi.png",
    "sim.png",
    "aSinicio.png"
]

# Função para o start 1 (executado uma única vez)
def start_1_func():
    print("Iniciando Start 1...")
    for imagem in start_1:
        procurar_e_clicar(imagem, caminho_base)

    executar_batalha()

# Função para o start 2 (executado em loop 42 vezes)
def start_2_func():
    print("Iniciando Start 2...")
    loop_count = 0
    while loop_count < 42:
        print(f"Iniciando a rodada {loop_count + 1} de 42 para Start 2.")
        for imagem in start_2:
            procurar_e_clicar(imagem, caminho_base)

        executar_batalha()

        loop_count += 1
        print(f"Rodada {loop_count} do Start 2 finalizada.")

# Função principal para procurar a imagem "select_instancia.png"
def iniciar_processos():
    start_1_concluido = False
    while True:
        select_instancia = pyautogui.locateOnScreen(f"{caminho_base}\\select_instancia.png", confidence=0.7)

        if select_instancia is not None and not start_1_concluido:
            print("Novo jogo iniciado! Iniciando Start 1...")
            start_1_func()
            start_1_concluido = True
        else:
            print("Aguardando fim de jogo...")

# Inicia a busca contínua pela imagem "select_instancia.png"
iniciar_processos()
