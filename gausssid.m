function [x2,k2,err2]=gausssid(a,b,p)
% x2 => vetor solução
% k2 => número de iterações
% a , b => matriz e vetor do sistema
% p => precisão
% err2 => matriz de erros
n=max(size(a));
k2=0;
err2 = []; % inicializa a matriz de erros
for i=1:n,
    x0(i)=0.5;
    s=0;
    for j=1:n,
        if j~=i,
            if j>i,
               s=s+abs(a(i,j));
            else
               s=s+bet(j)*abs(a(i,j));
            end,
        end,
    end,
    bet(i)=s/abs(a(i,i));
end,

if max(bet)<1,
    x2=x0;
    teste=1000;
    while teste>p,
        k2=k2+1;
        for i=1:n,
            s=0;
            for j=1:n,
                if j~=i,
                    s=s+a(i,j)*x2(j);
                end,
            end,
            x2(i)=(b(i)-s)/a(i,i);
        end,
        teste=max(abs(x2-x0));
        err2 = [err2; teste]; % adiciona o erro atual à matriz de erros
        x0=x2;
    end,
    x2=x2';
else
    x2='não converge';
end,

% exemplo de como chamar esta função
% a=[4 -1 -1 0;-1 4 0 -1;0 -1 -1 4];
% b=[45;55;40;50];
% p=1e-6;
% [x2,k2,err2]=gausssid(a,b,p)


