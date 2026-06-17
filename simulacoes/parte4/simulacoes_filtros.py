import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, butter, lfilter, freqz, tf2zpk, group_delay

PASTA_RESULTADOS = 'resultados'
os.makedirs(PASTA_RESULTADOS, exist_ok=True)

# Configurações globais
fs = 1000  # Frequência de amostragem
t = np.arange(0, 1.0, 1/fs)
nyq = 0.5 * fs


# Q1: Senoides e Filtro Passa-Baixa FIR

f1, f2 = 10, 200 # 10Hz e 200Hz
sinal_q1 = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# Filtro Passa-baixa fc = 50Hz
numtaps = 51
coefs_fir_q1 = firwin(numtaps, 50/nyq)
sinal_filtrado_q1 = lfilter(coefs_fir_q1, 1.0, sinal_q1)

plt.figure(figsize=(10, 4))
plt.plot(t[:100], sinal_q1[:100], label='Sinal Original (10Hz + 200Hz)')
plt.plot(t[:100], sinal_filtrado_q1[:100], label='Sinal Filtrado (Restou apenas 10Hz)', linewidth=2)
plt.title('Q1: Filtragem de Senoides (FIR)')
plt.xlabel('Tempo [s]')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig(os.path.join(PASTA_RESULTADOS, 'Q1_senoides.png'))
plt.close()


# Q2 e Q3: Ruído, FIR vs IIR Butterworth

sinal_limpo = np.sin(2 * np.pi * 5 * t)
ruido = np.random.normal(0, 0.5, len(t))
sinal_ruidoso = sinal_limpo + ruido

# FIR
coefs_fir_q2 = firwin(101, 20/nyq)
sinal_fir = lfilter(coefs_fir_q2, 1.0, sinal_ruidoso)

# IIR (Butterworth)
b_iir, a_iir = butter(4, 20/nyq, btype='low')
sinal_iir = lfilter(b_iir, a_iir, sinal_ruidoso)

plt.figure(figsize=(10, 6))
plt.subplot(2,1,1)
plt.plot(t, sinal_ruidoso, label='Com Ruído Branco', alpha=0.5)
plt.plot(t, sinal_fir, label='Filtrado FIR (Ordem 101)', linewidth=2)
plt.title('Q2 e Q3: Redução de Ruído - FIR vs IIR')
plt.legend(); plt.grid()

plt.subplot(2,1,2)
plt.plot(t, sinal_ruidoso, label='Com Ruído Branco', alpha=0.5)
plt.plot(t, sinal_iir, label='Filtrado IIR (Ordem 4)', linewidth=2, color='green')
plt.xlabel('Tempo [s]')
plt.legend(); plt.grid()
plt.tight_layout()
plt.savefig(os.path.join(PASTA_RESULTADOS, 'Q2_Q3_ruido.png'))
plt.close()


# Q4: Resposta em Frequência FIR vs IIR

w_fir, h_fir = freqz(coefs_fir_q2, worN=8000)
w_iir, h_iir = freqz(b_iir, a_iir, worN=8000)

plt.figure(figsize=(10, 4))
plt.plot(0.5 * fs * w_fir / np.pi, np.abs(h_fir), label='FIR')
plt.plot(0.5 * fs * w_iir / np.pi, np.abs(h_iir), label='IIR Butterworth')
plt.title('Q4: Resposta em Frequência (Magnitude)')
plt.xlabel('Frequência [Hz]')
plt.ylabel('Ganho')
plt.xlim(0, 50)
plt.legend(); plt.grid()
plt.savefig(os.path.join(PASTA_RESULTADOS, 'Q4_freq_response.png'))
plt.close()


# Q5: Polos e Zeros IIR

z, p, k = tf2zpk(b_iir, a_iir)

plt.figure(figsize=(5, 5))
plt.scatter(np.real(z), np.imag(z), marker='o', color='blue', label='Zeros')
plt.scatter(np.real(p), np.imag(p), marker='x', color='red', label='Polos')
circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--')
plt.gca().add_patch(circle)
plt.title('Q5: Polos e Zeros do Filtro IIR')
plt.xlabel('Real'); plt.ylabel('Imaginário')
plt.xlim(-1.5, 1.5); plt.ylim(-1.5, 1.5)
plt.legend(); plt.grid()
plt.savefig(os.path.join(PASTA_RESULTADOS, 'Q5_polos_zeros.png'))
plt.close()


# Q6: Resposta ao Impulso

impulso_sinal = np.zeros(100); impulso_sinal[0] = 1.0

imp_fir = lfilter(coefs_fir_q2, 1.0, impulso_sinal)
imp_iir = lfilter(b_iir, a_iir, impulso_sinal)

plt.figure(figsize=(10, 4))
plt.stem(imp_fir[:50], linefmt='b-', markerfmt='bo', basefmt='k-', label='FIR')
plt.stem(imp_iir[:50], linefmt='g-', markerfmt='go', basefmt='k-', label='IIR')
plt.title('Q6: Resposta ao Impulso')
plt.legend(); plt.grid()
plt.savefig(os.path.join(PASTA_RESULTADOS, 'Q6_impulso.png'))
plt.close()


# Q7: Filtro Passa-Faixa

# Sinal: 10Hz + 50Hz + 200Hz. Vamos isolar a de 50Hz
sinal_q7 = np.sin(2 * np.pi * 10 * t) + np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 200 * t)
b_pf, a_pf = butter(3, [40/nyq, 60/nyq], btype='band')
sinal_pf = lfilter(b_pf, a_pf, sinal_q7)

freqs = np.fft.fftfreq(len(t), 1/fs)
fft_orig = np.abs(np.fft.fft(sinal_q7))
fft_filt = np.abs(np.fft.fft(sinal_pf))

plt.figure(figsize=(10, 4))
plt.plot(freqs[:300], fft_orig[:300], label='Original')
plt.plot(freqs[:300], fft_filt[:300], label='Filtrado (Passa-faixa 50Hz)')
plt.title('Q7: Espectro Passa-Faixa')
plt.xlabel('Frequência [Hz]'); plt.legend(); plt.grid()
plt.savefig(os.path.join(PASTA_RESULTADOS, 'Q7_passa_faixa.png'))
plt.close()


# Q8 e Q9: Resposta de Fase e Atraso de Grupo

w, gd_fir = group_delay((coefs_fir_q2, 1.0))
w, gd_iir = group_delay((b_iir, a_iir))

plt.figure(figsize=(10, 4))
plt.plot(w / np.pi * nyq, gd_fir, label='FIR')
plt.plot(w / np.pi * nyq, gd_iir, label='IIR')
plt.title('Q8/Q9: Atraso de Grupo')
plt.xlabel('Frequência [Hz]'); plt.ylabel('Atraso em amostras')
plt.ylim(0, 100)
plt.legend(); plt.grid()
plt.savefig(os.path.join(PASTA_RESULTADOS, 'Q8_Q9_atraso_grupo.png'))
plt.close()

# Q10 & PBL: Monitoramento Agrícola (TinyML / Sensores)
# Simulando leitura de umidade no solo variando lentamente com forte ruído eletrônico
umidade_real = 40 + 10 * np.sin(2 * np.pi * 0.5 * t) # Variação lenta a 0.5Hz
ruido_sensor = np.random.normal(0, 3, len(t)) + 2*np.sin(2 * np.pi * 60 * t) # Ruído + rede 60Hz
leitura_sensor = umidade_real + ruido_sensor

# Filtro IIR pesado (útil para microcontroladores por exigir pouca memória)
b_pbl, a_pbl = butter(2, 5/nyq, btype='low')
leitura_filtrada = lfilter(b_pbl, a_pbl, leitura_sensor)

plt.figure(figsize=(10, 4))
plt.plot(t, leitura_sensor, color='gray', alpha=0.6, label='Sinal Bruto do Sensor (Ruidoso)')
plt.plot(t, umidade_real, 'k--', label='Umidade Real')
plt.plot(t, leitura_filtrada, 'r', linewidth=2, label='Sinal Filtrado (IIR)')
plt.title('PBL: Filtragem de Sensor de Umidade Agrícola')
plt.xlabel('Tempo [s]'); plt.ylabel('Umidade (%)')
plt.legend(); plt.grid()
plt.savefig(os.path.join(PASTA_RESULTADOS, 'PBL_agricultura.png'))
plt.close()

print(f"Simulações concluídas. Gráficos salvos com sucesso na pasta: {os.path.abspath(PASTA_RESULTADOS)}")