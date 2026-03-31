import numpy as np
import matplotlib.pyplot as plt

# 1. Representação de um sinal de sensor (Ex: Vibração Mecânica)
n = np.arange(0, 50)
f0 = 0.1 # Frequência Normalizada
x = np.sin(2 * np.pi * f0 * n) + 0.1 * np.random.randn(len(n)) # Sinal senoidal + ruído

# 2. Sistema de Média Móvel (Média de 3 Amostras)
# Este sistema é linear, invariante no tempo, estável e causal.
y = np.convolve(x, [1/3, 1/3, 1/3], mode='same')

# 3. Geração de Gráficos
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.stem(n, x, label='Sinal Bruto x[n]')
plt.title('Aquisição de Sinal de Sensor Industrial')
plt.legend()
plt.subplot(2, 1, 2)
plt.stem(n, y, linefmt='r', label='Sinal Filtrado y[n]')
plt.title('Saída do Sistema (Filtro de Média Móvel)')
plt.legend()
plt.tight_layout()
plt.savefig('./resultados/grafico_sensor.png')
plt.show()
