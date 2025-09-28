# 📊 Análise Comparativa dos Algoritmos de Criptografia

## 📈 Comparação entre Tamanho da Mensagem (MB) e Tempo de Execução (ms)

O gráfico a seguir compara o tempo de encriptação e decriptação dos algoritmos **DES**, **RSA** e **Goldwasser-Micali (GM)** em função do **tamanho da mensagem**.

![Gráfico comparativo](resultado.png)

---

## 🧠 Análise Qualitativa

Analisando o gráfico, notamos uma grande diferença entre o **DES** e os demais algoritmos:

- 🔹 **DES** é o **mais eficiente**, pois mantém um **crescimento linear suave** mesmo com o aumento do tamanho da mensagem.
- 🔹 **RSA** e **Goldwasser-Micali (GM)** apresentam curvas de crescimento **muito mais acentuadas**:  
  quanto maior a mensagem, maior o tempo necessário para criptografar e descriptografar.
- 🔹 Entre os dois, o **GM** é o que apresenta **pior desempenho**, mostrando um crescimento exponencial nos tempos conforme o tamanho dos dados aumenta.

Em resumo:
- **DES** é o mais rápido e escalável;
- **RSA** é intermediário, viável apenas para mensagens pequenas ou para cifrar chaves;
- **GM** é o mais lento, de uso mais teórico.

---

## 📉 Análise Quantitativa

### 1. 🧾 Valores aproximados

| Tamanho (MB) | DES (ms) | RSA (ms) | GM (ms) |
|--------------|-----------|----------|---------|
| 0.1          | ~5        | ~200     | ~10.000 |
| 0.5          | ~25       | ~1.000   | ~50.000 |
| 1.0          | ~50       | ~2.000   | ~100.000 |

Mesmo que todos cresçam de forma linear, os valores absolutos são muito diferentes.

---

### 2. 📊 Relações de desempenho

Para **1 MB**:
- **RSA** é cerca de **40× mais lento** que o **DES**  
- **GM** é cerca de **2.000× mais lento** que o **DES**

Para **0.1 MB**, essa proporção se mantém, mostrando que o fator de lentidão é **constante** ao longo do crescimento.

---

### 3. ⚙️ Tempo por MB (eficiência)

| Algoritmo | Tempo por MB (ms/MB) |
|------------|------------------------|
| DES        | ~50                   |
| RSA        | ~2.000                |
| GM         | ~100.000              |

Ou seja:
- **DES** → 1 MB em **0,05 s**
- **RSA** → 1 MB em **2 s**
- **GM** → 1 MB em **100 s**

---

### 4. 📈 Crescimento percentual (0.1 MB → 1 MB)

| Algoritmo | Crescimento (%) |
|------------|------------------|
| DES        | +900%            |
| RSA        | +900%            |
| GM         | +900%            |

Todos apresentam crescimento **linear** (mesmo percentual), mas com bases de custo muito diferentes.

---

### 5. 💡 Implicações práticas

Para mensagens de **1 MB**:
- **DES** → cerca de **50 ms** → **instantâneo**
- **RSA** → cerca de **2.000 ms (2 s)** → **aceitável apenas para chaves ou pequenos blocos**
- **GM** → cerca de **100.000 ms (100 s)** → **inviável na prática**

Portanto, o uso de **sistemas híbridos** é ideal:
- Utilizar **RSA** apenas para **criptografar a chave de sessão**
- Utilizar **DES (ou AES)** para **criptografar o conteúdo real**

---

## ✅ Conclusão

- O **DES** apresenta **melhor escalabilidade** e **eficiência** entre os três.
- O **RSA** tem desempenho **moderado**, adequado para tarefas específicas.
- O **Goldwasser-Micali** é **muito ineficiente**, servindo mais para estudos acadêmicos.

Em termos de **desempenho relativo**:
- **DES** ≫ **RSA** ≫ **GM**

Essa análise confirma a importância de escolher o algoritmo conforme o **contexto de uso**, levando em conta o **tamanho da mensagem**, **tempo de execução** e **custo computacional**.
