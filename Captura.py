import time, json
from pynput import mouse, keyboard

eventos = []
inicio = time.time()
teclas_abertas = {}

def t(): return round(time.time() - inicio, 3)

def on_click(x, y, botao, pressionado):
    if pressionado:
        eventos.append({"t": t(), "tipo": "clique", "x": x, "y": y})

def on_press(k):
    nome = getattr(k, "char", None) or str(k)
    if nome not in teclas_abertas:
        teclas_abertas[nome] = t()

def on_release(k):
    nome = getattr(k, "char", None) or str(k)
    if nome in teclas_abertas:
        ini = teclas_abertas.pop(nome)
        eventos.append({"t": ini, "tipo": "tecla", "tecla": nome, "duracao": round(t() - ini, 3)})
    if k == keyboard.Key.esc:  # ESC encerra e salva
        with open("gravacao.json", "w") as f:
            json.dump(eventos, f, indent=2)
        return False

with mouse.Listener(on_click=on_click) as ml, \
     keyboard.Listener(on_press=on_press, on_release=on_release) as kl:
    kl.join()