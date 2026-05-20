x_ruido = x + 0.5*randn(1, N);
X = fft(x_ruido);
plot(f, abs(X)); title('Sinal com Ruído Aditivo');
% Discussão: FFT ajuda a identificar a frequência mesmo com ruído.
