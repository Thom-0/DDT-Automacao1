import pyautogui
import time
import os

# Caminho base das imagens
caminho_base = r"E:\Projetos\DDT-Automacaoo\imagens\Trial_2"

# Função para procurar e clicar em uma imagem
def procurar_e_clicar(imagem, caminho_base, tempo_espera=1):
    caminho_completo = os.path.join(caminho_base, imagem)
    print(f"Procurando: {caminho_completo}")

    botao = pyautogui.locateOnScreen(caminho_completo, confidence=0.8)
    
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
            batalha = pyautogui.locateOnScreen(os.path.join(caminho_base, "batalha_iniciada.png"), confidence=0.7)
        except pyautogui.ImageNotFoundException:
            print("Imagem de batalha não encontrada.")
            time.sleep(1)
    
    # Quando a batalha é encontrada, começa a procurar pela seta de batalha
    Seta_de_batalha = None
    while Seta_de_batalha is None:
        try:
            Seta_de_batalha = pyautogui.locateOnScreen(os.path.join(caminho_base, "Seta_de_batalha.png"), confidence=0.7)
            if Seta_de_batalha is not None:
                pyautogui.click(pyautogui.center(Seta_de_batalha))
                print("Seta de batalha encontrada e clicada.")
            time.sleep(1)
        except pyautogui.ImageNotFoundException:
            print("Imagem da Seta de Batalha não encontrada.")
            time.sleep(1)
    
    # Agora, começa a procurar pela imagem "Sua vez" enquanto houver batalha
    while batalha is not None:
        sua_vez = None
        while sua_vez is None:
            try:
                sua_vez = pyautogui.locateOnScreen(os.path.join(caminho_base, "sua_vez.png"), confidence=0.7)
                if sua_vez is not None:
                    # Pressiona as teclas enquanto estiver "Sua vez"
                    teclas_numero = ['num1', 'num2', 'num4']
                    for tecla in teclas_numero:
                        pyautogui.press(tecla)  # Pressiona a tecla
                        time.sleep(0.05)  # Espera 0.2 segundos entre cada tecla
                    print("Teclas pressionadas para 'Sua vez'.")
                    
                    pyautogui.keyDown("space")
                    time.sleep(1.9)  # Mantém pressionado por 3 segundos
                    pyautogui.keyUp("space")
                    time.sleep(1)  # Espera 1 segundo antes de procurar novamente

            except pyautogui.ImageNotFoundException:
                print("Imagem 'Sua vez' não encontrada.")
                pass

            # Procura pelo "Fim do Jogo" após cada rodada de batalha
            fim_do_jogo = None
            try:
                fim_do_jogo = pyautogui.locateOnScreen(os.path.join(caminho_base, "fim_do_Jogo.png"), confidence=0.7)
                if fim_do_jogo:
                    print("Fim do jogo detectado.")
                    time.sleep(20)  # Aguarda 20 segundos antes de reiniciar o processo
                    break  # Sai do loop de batalha e reinicia o processo
            except pyautogui.ImageNotFoundException:
                print("Imagem 'Fim do Jogo' não encontrada, tentando novamente...")
                time.sleep(5)

        # Se "Fim do Jogo" for encontrado, pausa até a próxima batalha
        if fim_do_jogo:
            print("Aguardando nova batalha...")
            time.sleep(3)  # Espera 20 segundos antes de iniciar o start 2

            # Inicia o start 2 após 20 segundos de espera
            start_2_func()

# Lista de imagens para o start 1
start_1 = [
    "select_instancia.png",
    "ins_unica.png",
    "ins_trial2.png",
    "modo_heroi.png",
    "sim.png",
    "aSinicio.png"
]

# Lista de imagens para o start 2
start_2 = [
    "select_instancia.png",
    "ins_trial2.png",
    "modo_heroi.png",
    "sim.png",
    "aSinicio.png"
]

# Função para o start 1 (executado uma única vez)
def start_1_func():
    print("Iniciando Start 1...")
    for imagem in start_1:
        procurar_e_clicar(imagem, caminho_base)
    
    # Executa a função de batalha uma vez após o Start 1
    executar_batalha()

# Função para o start 2 (executado em loop 42 vezes)
def start_2_func():
    print("Iniciando Start 2...")
    loop_count = 0
    while loop_count < 42:
        print(f"Iniciando a rodada {loop_count + 1} de 42 para Start 2.")
        for imagem in start_2:
            procurar_e_clicar(imagem, caminho_base)
        
        # Executa a função de batalha após o Start 2
        executar_batalha()
        
        loop_count += 1
        print(f"Rodada {loop_count} do Start 2 finalizada.")

# Função principal para procurar a imagem "select_instancia.png"
def iniciar_processos():
    start_1_concluido = False
    while True:
        select_instancia = pyautogui.locateOnScreen(os.path.join(caminho_base, "select_instancia.png"), confidence=0.7)
        
        if select_instancia is not None and not start_1_concluido:
            print("Novo jogo iniciado! Iniciando Start 1...")
            start_1_func()  # Inicia o Start 1
            start_1_concluido = True  # Marca que o Start 1 foi concluído
        else:
            print("Aguardando fim de jogo...")
            time.sleep(3)

# Inicia a busca contínua pela imagem "select_instancia.png"
iniciar_processos()
