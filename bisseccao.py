import math

def f(x):
    return math.cos(x)**3 - math.sin(x)

def bissecao(a, b, epsilon):
    if f(a) * f(b) >= 0:
        print("A função não muda de sinal nos pontos a e b.")
        return None, None, None, None

    num_iteracoes = 0

    while (b - a) > epsilon:
        c = (a + b) / 2

        if f(c) == 0:
            return c, f(c), (b - a) / 2, num_iteracoes

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        num_iteracoes += 1

    media_amostral = (a + b) / 2
    valor_medio_amostral = f(media_amostral)
    erro_x = (b - a) / 2

    return media_amostral, valor_medio_amostral, erro_x, num_iteracoes

# Intervalo inicial [a, b]
a = 0
b = 1

# Precisão desejada
epsilon = 1e-6

media_amostral, valor_medio_amostral, erro_x, num_iteracoes = bissecao(a, b, epsilon)

if media_amostral is not None:
    print("Média amostral:", media_amostral)
    print("f(média amostral):", valor_medio_amostral)
    print("Erro em x:", erro_x)
    print("Número de iterações:", num_iteracoes)
else:
    print("Não foi encontrada uma raiz no intervalo dado.")
