% Simulação de vibração mecânica com ruído e tendência
t = 0:0.001:1;
vib = sin(2*pi*50*t) + 0.2*randn(size(t));
plot(abs(fft(vib))); title('Análise Espectral de Vibração Simulada');
