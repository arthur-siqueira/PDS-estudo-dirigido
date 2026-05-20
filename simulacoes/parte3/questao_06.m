x_curto = [1 2 3 4]; N_c = length(x_curto);
% DFT Direta
X_direta = zeros(1, N_c);
for k = 0:N_c-1
    for n_idx = 0:N_c-1
        X_direta(k+1) = X_direta(k+1) + x_curto(n_idx+1)*exp(-j*2*pi*k*n_idx/N_c);
    end
end
X_fft = fft(x_curto);
disp(X_direta); disp(X_fft); % Comparação de valores

subplot(2,1,1);
stem(abs(X_direta), 'filled'); title('Magnitude: DFT Direta');
ylabel('|X(k)|'); grid on;

subplot(2,1,2);
stem(abs(X_fft), 'r--o'); title('Magnitude: FFT do Octave');
ylabel('|X(k)|'); grid on;

% Salva o gráfico para a sua pasta de resultados
print('-dpng', '../../resultados/parte_3/q06_comparacao_dft_fft.png');
