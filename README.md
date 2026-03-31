# Processamento Digital de Sinais - Estudo Dirigido

[cite_start]Este repositório contém as atividades desenvolvidas para a disciplina de Processamento Digital de Sinais (PDS) do curso de Engenharia da Computação - IFPB[cite: 1, 4, 138]. [cite_start]O estudo segue a metodologia PBL (Problem Based Learning)[cite: 14, 183].

## Parte 1 - Modelagem de Sinais e Sistemas Discretos

### 📋 Descrição da Etapa
[cite_start]Nesta etapa inicial, o foco foi a compreensão dos fundamentos matemáticos para representação de sinais discretos e a classificação de sistemas conforme suas propriedades estruturais[cite: 140, 144].

### 🧠 Resumo Teórico
[cite_start]Os sinais discretos são interpretados como sequências numéricas $x[n]$ provenientes da amostragem de fenômenos físicos[cite: 38, 148]. A modelagem envolve a análise de propriedades como:
* [cite_start]**Linearidade:** Obediência aos princípios de superposição e homogeneidade[cite: 151, 161].
* [cite_start]**Causalidade:** Onde a saída depende apenas de valores atuais ou passados da entrada[cite: 151, 162].
* [cite_start]**Estabilidade BIBO:** Garantia de que entradas limitadas gerem saídas limitadas, evitando divergências no processamento[cite: 45, 166].

### 💻 Atividades Desenvolvidas
1. [cite_start]**Resumo Técnico:** Elaboração de fundamentação teórica baseada em Oppenheim e Lathi[cite: 28, 132, 134].
2. [cite_start]**Simulação Computacional:** Implementação de um script Python para simular a aquisição de dados de um sensor real (vibração) e aplicação de um sistema de média móvel para filtragem[cite: 178, 192].
3. [cite_start]**Análise de Resultados:** Geração de gráficos comparativos entre o sinal bruto (com ruído) e o sinal processado[cite: 193, 194].

### 🎯 Resposta ao Problema Norteador
[cite_start]**Pergunta:** Como representar matematicamente o comportamento temporal de um sensor real e quais propriedades estruturais devem ser analisadas para garantir o correto processamento digital desse sinal? [cite: 184]

[cite_start]**Resposta:** Um sensor real é representado matematicamente como uma **sequência discreta $x[n]$** obtida através do processo de amostragem[cite: 148]. Para garantir o correto processamento digital, o sistema deve ser:
* [cite_start]**Estável (BIBO):** Para que o algoritmo não divirja, garantindo a integridade dos dados e do hardware[cite: 166, 204].
* [cite_start]**Causal:** Propriedade mandatória para implementação em tempo real em sistemas embarcados (como o ESP32), visto que o sistema não pode prever valores futuros do sensor para calcular a saída atual[cite: 162, 204].

## 📂 Organização do Repositório
* [cite_start]`/teoria`: Resumo teórico fundamentado[cite: 196].
* [cite_start]`/simulacoes`: Códigos das simulações devidamente comentados.
* [cite_start]`/resultados`: Gráficos e discussão dos dados obtidos[cite: 193, 198].
