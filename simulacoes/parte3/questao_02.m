f1 = 0.1; f2 = 0.25;
x = sin(2*pi*f1*n) + sin(2*pi*f2*n);
X = fft(x);
plot(f, abs(X)); title('Espectro de Duas Senoides');
% Discussão: FFT separa as frequências que no tempo parecem misturadas.
