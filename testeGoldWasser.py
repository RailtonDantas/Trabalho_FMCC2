from algoritmos_criptografia.goldwasser import encrypt,decrypt,generate_key,int_encode_str,int_encode_char,int_to_bool_list,int_decode_str
import psutil
import time
import os
import pandas as pd
import gc
import statistics


lista_tamanhos_mensagens = list(range(10000,1010000,10000))
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

    gc.collect()
    time.sleep(0.01)

    memoria_antes = []
    for _ in range(5):
        memoria_antes.append(process.memory_info().rss)
        time.sleep(0.001)
    memoria_antes = sum(memoria_antes)/5

    tempo_inicial = time.perf_counter()

    key = generate_key()
    msg_encode = int_encode_str(msg)

    dados = encrypt(m=msg_encode,pub_key=key['pub'])
    dados_decriptados_int = decrypt(dados,priv_key=key['priv'])
    #dados_decriptados_str = int_decode_str(dados_decriptados_int)

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
    del key,dados,dados_decriptados_int
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
df.to_csv("resultado_Goldwasser-micali.csv")
