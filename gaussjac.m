function [x,k,err]=gaussjac(a,b,p)
% x => vetor solução
% k => número de iterações
% a , b => matriz e vetor do sistema
% p => precisão
% err => matriz de erros
n=max(size(a));
k=0;
err = []; % inicializa a matriz de erros
for i=1:n,
    x0(i)=0.5;
    s=0;
    for j=1:n,
        if j~=i,
            s=s+abs(a(i,j));
        end,
    end,
    alf(i)=s/abs(a(i,i));
end,

if max(alf)<1,	
    teste=1000;
    while teste>p,
        k=k+1;
        for i=1:n,
            s=0;
            for j=1:n,
                if j~=i,
                    s=s+a(i,j)*x0(j);
                end,
            end,
            x(i)=(b(i)-s)/a(i,i);
        end,
        teste=max(abs(x-x0));
        err = [err; teste]; % adiciona o erro atual à matriz de erros
        x0=x;
        %[x0 teste]
    end,
    x=x';
else
    x='não converge';
end,

% exemplo de como chamar esta função
% a=[4 -1 -1 0;-1 4 0 -1;0 -1 -1 4];
% b=[45;55;40;50];
% p=1e-6;
% [x,k,err]=gaussjac(a,b,p)
