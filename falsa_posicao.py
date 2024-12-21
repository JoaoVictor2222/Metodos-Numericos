import math


def f(x):
    return math.cos(x) ** 3 - math.sin(x)


def falsa_posicao(a, b, tol):
    if f(a) * f(b) >= 0:
        print("O método da falsa posição não é aplicável neste intervalo.")
        return None

    iteracoes = 0
    erro_x = abs(b - a)

    while erro_x > tol:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if f(c) == 0:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        iteracoes += 1
        erro_x = abs(b - a)

        media_amostral = (a + b) / 2
        f_media_amostral = f(media_amostral)

        print("Iteração:", iteracoes)
        print("Média amostral:", media_amostral)
        print("f(Média amostral):", f_media_amostral)
        print("Erro em x:", erro_x)
        print()

    return media_amostral, f_media_amostral, erro_x, iteracoes


# Testando o método da falsa posição para encontrar uma raiz da função f(x)
a = 0
b = 1
tolerancia = 0.0001

resultado = falsa_posicao(a, b, tolerancia)

if resultado is not None:
    media_amostral, f_media_amostral, erro_x, iteracoes = resultado
    print("Raiz aproximada:", media_amostral)
    print("f(Raiz aproximada):", f_media_amostral)
    print("Erro em x:", erro_x)
    print("Número de iterações:", iteracoes)
