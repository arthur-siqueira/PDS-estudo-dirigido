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

## 📂 Organização do Repositório
* `/teoria`: Resumo teórico fundamentado e definições matemáticas.
* `/simulacoes`: Códigos das simulações devidamente comentados.
* `/resultados`: Gráficos, imagens e discussão dos resultados obtidos.
