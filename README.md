# Processamento Digital de Sinais - Estudo Dirigido

Este repositório contém as atividades desenvolvidas para a disciplina de Processamento Digital de Sinais (PDS) do curso de Engenharia da Computação - IFPB. O desenvolvimento segue a metodologia PBL (Problem Based Learning), integrando teoria e prática em sistemas computacionais e embarcados.

## Parte 1 - Modelagem de Sinais e Sistemas Discretos

### 📋 Descrição da Etapa
Esta etapa inicial teve como objetivo a compreensão dos fundamentos matemáticos para a representação de sinais discretos e a classificação de sistemas conforme suas propriedades estruturais.

### 🧠 Resumo Teórico
Sinais discretos são sequências numéricas obtidas por amostragem de fenômenos físicos. A modelagem envolve a análise de propriedades fundamentais que determinam o comportamento da relação entrada-saída:
* **Linearidade:** Obediência aos princípios de superposição e homogeneidade.
* **Causalidade:** A saída atual depende apenas de valores de entrada presentes ou passados.
* **Estabilidade BIBO:** Garantia de que entradas limitadas gerem saídas limitadas, essencial para evitar divergências em microcontroladores.
* **Invariância no Tempo:** As propriedades do sistema permanecem constantes ao longo do tempo.

### 💻 Atividades Desenvolvidas
1. **Resumo Técnico:** Elaboração de fundamentação teórica baseada na bibliografia de Oppenheim e Lathi.
2. **Simulação Computacional:** Implementação de script em Python para simular a aquisição de um sensor real (vibração) e aplicação de um sistema de média móvel para suavização do sinal.
3. **Análise de Resultados:** Geração de gráficos comparativos entre o sinal bruto e o sinal filtrado.

### 🎯 Resposta ao Problema Norteador
**Pergunta:** Como representar matematicamente o comportamento temporal de um sensor real e quais propriedades estruturais devem ser analisadas para garantir o correto processamento digital desse sinal?

**Resposta:** Um sensor real é representado matematicamente como uma **sequência discreta x[n]** obtida por amostragem. Para garantir o correto processamento digital, o sistema deve ser:
* **Estável (BIBO):** Para garantir que o sinal não divirja, preservando a integridade do processamento e do hardware.
* **Causal:** Propriedade obrigatória para implementação em tempo real (como no ESP32), pois o sistema não pode depender de valores futuros do sensor para calcular a saída atual.

---

## Parte 3 – Análise no Domínio da Frequência

### 📋 Descrição da Etapa
Esta etapa teve como objetivo introduzir os fundamentos da análise espectral de sinais discretos. O foco principal foi compreender como a informação de um sinal pode ser representada e interpretada no domínio da frequência, permitindo identificar componentes e padrões que não são visíveis no domínio do tempo.

### 🧠 Resumo Teórico
A análise de frequência permite entender como a energia de um sinal está distribuída entre diferentes componentes espectrais:
* **DTFT e DFT:** Enquanto a DTFT é uma função contínua da frequência, a DFT é a sua versão amostrada, essencial para o processamento numérico em computadores.
* **Algoritmo FFT:** Uma implementação matematicamente otimizada da DFT que reduz drasticamente o custo computacional, tornando viável o processamento em tempo real em sistemas embarcados.
* **Transformada-Z:** Estende a análise para o plano complexo, sendo a ferramenta fundamental para investigar a estabilidade de sistemas digitais através da localização de polos e zeros.
* **Fenómenos de Análise:** O estudo abordou o **Aliasing** (distorção por taxa de amostragem insuficiente) e o **Janelamento**, técnica utilizada para reduzir o vazamento espectral em sinais de duração finita.

### 💻 Atividades Desenvolvidas
1. **Resumo Técnico:** Elaboração de síntese teórica sobre transformadas (DFT/FFT/Z) e fenómenos espectrais baseada em Oppenheim e Proakis.
2. **Simulação Computacional:** Implementação em Octave de scripts para geração de senoides, soma de sinais, análise de aliasing e aplicação de janelas de Hamming.
3. **Análise de Estabilidade:** Determinação numérica da resposta ao impulso de sistemas discretos e análise de convergência no plano-z.
4. **Processamento de Sinais Reais:** Aplicação da FFT em sinais simulados de vibração para identificação de harmónicas e diagnóstico de falhas.

### 🎯 Resposta ao Problema Norteador
**Pergunta:** Como identificar, a partir do conteúdo espectral de um sinal real, informações relevantes sobre o comportamento dinâmico de um sistema físico e quais limitações práticas devem ser consideradas durante a aquisição e análise desses dados?

**Resposta:** A identificação é feita através da localização e magnitude dos picos no espectro de frequência (via FFT), que revelam frequências fundamentais e harmónicas associadas a fenómenos físicos, como a rotação de um motor ou vibrações estruturais. As principais limitações práticas incluem:
* **Resolução Espectral:** É limitada pelo número de amostras (N); quanto menor o tempo de aquisição, menos definidos são os picos espectrais.
* **Aliasing:** Se a taxa de amostragem for inferior ao limite de Nyquist, as informações de alta frequência serão "dobradas" para frequências baixas, corrompendo os dados.
* **Vazamento Espectral:** O truncamento de sinais reais introduz componentes espúrias, exigindo o uso de janelamento (como Hamming) para suavizar as transições e aumentar a fidelidade do espectro.

## 📂 Organização do Repositório
* `/teoria`: Resumo teórico fundamentado e definições matemáticas.
* `/simulacoes`: Códigos das simulações devidamente comentados.
* `/resultados`: Gráficos, imagens e discussão dos resultados obtidos.
