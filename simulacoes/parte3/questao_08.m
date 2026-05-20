N1 = 64; N2 = 512;
x1 = sin(2*pi*0.1*(0:N1-1)); x2 = sin(2*pi*0.1*(0:N2-1));
subplot(2,1,1); plot(abs(fft(x1))); title('N=64 (Baixa Resolução)');
subplot(2,1,2); plot(abs(fft(x2))); title('N=512 (Alta Resolução)');
