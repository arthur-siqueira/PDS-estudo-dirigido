x = sin(2*pi*0.15*n);
X_ret = fft(x); % Sem janela (Retangular)
X_ham = fft(x .* hamming(N)'); % Com janela Hamming
plot(f, 20*log10(abs(X_ret)), f, 20*log10(abs(X_ham)));
legend('Sem Janela', 'Hamming'); title('Vazamento Espectral');
