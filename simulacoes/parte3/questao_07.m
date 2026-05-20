b = [1]; a = [1, -0.8];
h = filter(b, a, [1 zeros(1, 49)]); % Resposta ao impulso
stem(0:49, h); title('Resposta ao Impulso - Sistema Estável');
