N = 128; f0 = 0.1; n = 0:N-1;
x = sin(2*pi*f0*n);
X = fft(x);
f = (0:N-1)/N;
subplot(2,1,1); stem(n, x); title('Domínio do Tempo');
subplot(2,1,2); plot(f, abs(X)); title('Espectro (FFT)');
grid on; % Frequência dominante em 0.1
