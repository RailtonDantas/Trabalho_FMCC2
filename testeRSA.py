import psutil
import time
import os
import pandas as pd
import gc
import statistics
from algoritmos_criptografia.RSA import RivestShamirAdleman

lista_tamanhos_mensagens = list(range(10000,1000000,10000))
matriz = []
for tamanho in lista_tamanhos_mensagens:
    gc.collect()
    print(tamanho)

    process = psutil.Process(os.getpid())
    row = []
    msg = "A"*tamanho
    mb = len(msg.encode("utf-8"))/(1024**2) 
    mb = f'{mb:.2f}'
    

    tempos = []
    memorias = []

    for exe in range(3):
        gc.collect()
        time.sleep(0.01)

        memoria_antes = []
        for _ in range(5):
            memoria_antes.append(process.memory_info().rss)
            time.sleep(0.001)
        memoria_antes = sum(memoria_antes)/5

        tempo_inicial = time.perf_counter()

        cifra = RivestShamirAdleman(size_key=2048)
        dados = cifra.encriptar(msg)
        cifra.decriptar(dados)

        tempo_final = time.perf_counter()
        time.sleep(0.01)
        memoria_depois = []
        for _ in range(5):
            memoria_depois.append(process.memory_info().rss)
            time.sleep(0.001)
        memoria_depois = sum(memoria_depois)/5

        tempo_gasto = (tempo_final - tempo_inicial)*1000
        mem_gasta = (memoria_depois - memoria_antes)/(1024**2)

        memorias.append(mem_gasta)
        tempos.append(tempo_gasto)
        del cifra,dados
        gc.collect()

    media_memoria = statistics.median(memorias)
    media_tempos = statistics.median(tempos)
    if abs(media_memoria) < 0.01:
            media_memoria = round(media_memoria, 4)

    if abs(media_tempos) < 0.01:
            media_tempos = round(media_tempos, 4)
    row = {
        'Tamanho_msg_caracteres':tamanho,
        'Tamanho_msg_MB':mb,
        'Tempo_gasto_ms':media_tempos,
        'Memoria_gasta_MB':media_memoria

    }
    matriz.append(row)

    

df = pd.DataFrame(matriz)
df.to_csv("resultado_RSA.csv")