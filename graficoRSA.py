import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv('resultado_RSA.csv')

tamanho_mb = df['Tamanho_msg_MB']
tempo_ms = df['Tempo_gasto_ms']
tempo_ms = tempo_ms.map(lambda x: x//1000)

fig = plt.figure(figsize=(10,5))
plt.title("Gráfico que relaciona tempo de encriptação e decriptação e\n tamanho da mensagem encriptada/decriptada\nAlgoritmo RSA",fontdict={
    'fontsize':10,'fontstyle':'italic','color':'black'
})

plt.ylabel("Tempo gasto (s)",fontdict={
    'fontsize':10,'fontstyle':'italic','color':'black'
})
plt.xlabel("Tamanho da mensagem (MB)",fontdict={
    'fontsize':10,'fontstyle':'italic','color':'black'
})
plt.yticks(pd.Series(range(0,32,2)))
plt.xticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95])
line = plt.plot(tamanho_mb,tempo_ms,color='black')[0]
line.set_linestyle('solid')
line.set_marker('o')
line.set_markersize(3.5)
line.set_markerfacecolor('gray')
line.set_linewidth(2)


plt.tight_layout()
plt.show()
