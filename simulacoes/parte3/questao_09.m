f_fund = 0.1;
x = sin(2*pi*f_fund*n) + 0.5*sin(2*pi*2*f_fund*n); % Fundamental + 2ª Harmônica
plot(f, abs(fft(x))); title('Análise de Harmônicas');
