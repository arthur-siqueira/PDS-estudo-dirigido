fs = 100; f_sinal = 80; % f_sinal > fs/2 causa aliasing
t = 0:1/fs:1;
x = sin(2*pi*f_sinal*t);
X = fft(x);
plot(abs(X)); title('Efeito de Aliasing (f_sinal > fs/2)');
