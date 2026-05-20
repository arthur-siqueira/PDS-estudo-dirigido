# Parte 3 – Análise no Domínio da Frequência

## Descrição das Atividades
Nesta etapa, realizei a análise espectral de sinais discretos utilizando o software Octave para visualizar e interpretar o comportamento de diferentes sistemas e sinais no domínio da frequência.

---

## Questão 1: FFT de uma Senoide
**Objetivo:** Gerar uma senoide de $f_0=0,1$ e observar o seu espectro.

<img src="resultados/parte3/q01_espectro.png" alt="Imagem do resultado da questão 01">

**Discussão Técnica:** Ao aplicar a FFT numa senoide pura, observa-se um pico nítido na frequência normalizada correspondente a $0,1$. Isto demonstra como a energia do sinal está concentrada numa única componente espectral, permitindo a sua identificação precisa no domínio da frequência.

---

## Questão 2: Soma de Senoides
**Objetivo:** Gerar duas senoides de frequências distintas e analisar o sinal resultante.

![Gráfico Questão 2](q02_soma_senoides.png)

**Discussão Técnica:** Embora no domínio do tempo a soma das senoides apresente uma forma de onda mais complexa, a FFT permite distinguir claramente as duas componentes de frequência independentes. Este resultado evidencia a utilidade da representação espectral para decompor sinais que parecem misturados no tempo.

---

## Questão 3: Fenómeno de Aliasing
**Objetivo:** Analisar o efeito da redução da taxa de amostragem num sinal de frequência elevada.

![Gráfico Questão 3](q03_aliasing_efeito.png)

**Discussão Técnica:** O aliasing ocorre quando a frequência de amostragem é insuficiente para representar o conteúdo espectral do sinal (abaixo do limite de Nyquist). No gráfico, percebe-se que a frequência original "reaparece" numa posição errada do espectro, causando uma distorção irreversível na interpretação do sinal.

---

## Questão 4: Janelamento e Vazamento Espectral
**Objetivo:** Comparar o sinal sem janela com a aplicação de uma janela de Hamming.

![Gráfico Questão 4](q04_janelamento_hamming.png)

**Discussão Técnica:** O truncamento de sinais finitos introduz descontinuidades que geram o "vazamento espectral". A aplicação da janela de Hamming suaviza estas extremidades, reduzindo significativamente os lobos laterais e melhorando a precisão da análise.

---

## Questão 5: Sinal com Ruído
**Objetivo:** Identificar a frequência principal num sinal corrompido por ruído aditivo.

![Gráfico Questão 5](q05_sinal_com_ruido.png)

**Discussão Técnica:** A análise espectral auxilia na separação entre a componente útil e as perturbações. Mesmo com ruído dificultando a visualização no tempo, a FFT revela um pico nítido na frequência do sinal, provando ser uma ferramenta poderosa para deteção.

---

## Questão 6: Equivalência DFT vs FFT
**Objetivo:** Comparar a implementação direta da DFT com o algoritmo FFT.

![Gráfico Questão 6](q06_comparacao_dft_fft.png)

**Discussão Técnica:** Os resultados numéricos obtidos por ambos os métodos são idênticos, validando a equivalência matemática. No entanto, a FFT é drasticamente mais eficiente, reduzindo o custo computacional e tornando viável o processamento em tempo real.

---

## Questão 7: Estabilidade do Sistema (Plano-Z)
**Objetivo:** Determinar a resposta ao impulso de $H(z) = \frac{1}{1 - 0.8z^{-1}}$.

![Gráfico Questão 7](q07_resposta_impulso.png)

**Discussão Técnica:** O sistema é considerado estável porque a sua resposta ao impulso decai exponencialmente para zero. No plano-z, isto corresponde a ter o polo ($z=0,8$) localizado dentro do círculo unitário, o que garante a estabilidade do sistema.

---

## Questão 8: Resolução Espectral
**Objetivo:** Comparar a resolução espectral para sinais com diferentes durações ($N$).

![Gráfico Questão 8](q08_resolucao_espectral.png)

**Discussão Técnica:** Observou-se que um maior número de amostras ($N$) resulta numa resolução espectral mais fina. Sinais mais longos permitem definir picos de frequência com maior precisão, enquanto sinais curtos apresentam picos mais largos.

---

## Questão 9: Análise de Harmónicas
**Objetivo:** Identificar frequências fundamentais e harmónicas num sinal complexo.

![Gráfico Questão 9](q09_analise_harmonicas.png)

**Discussão Técnica:** A capacidade de identificar harmónicas é fundamental no diagnóstico de falhas mecânicas e vibrações. O espectro permite visualizar múltiplos da frequência fundamental, o que ajuda a detetar irregularidades em equipamentos industriais.

---

## Questão 10: Análise de Sinal Real
**Objetivo:** Implementar a análise espectral de um sinal real ou simulado.

![Gráfico Questão 10](q10_sinal_real_vibracao.png)

**Discussão Técnica:** A aplicação dos conceitos a um sinal real permitiu extrair informações sobre o comportamento dinâmico do sistema através dos picos espectrais. Esta interpretação é a base para o diagnóstico industrial e processamento de sinais em engenharia.
