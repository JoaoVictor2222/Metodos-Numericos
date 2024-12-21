import math

def f(x):
    return math.cos(x)**3 - math.sin(x)

def df(x):
    return -3*math.cos(x)**2*math.sin(x) - math.cos(x)

def newton_raphson(f, df, x0, epsilon, max_iter):
    x = x0
    iterations = 0
    while True:
        fx = f(x)
        if abs(fx) < epsilon:
            break
        dfx = df(x)
        if dfx == 0:
            break
        x_prev = x
        x = x - fx/dfx
        iterations += 1
    return x, f(x), abs(x - x_prev), iterations

# Valores iniciais
x0 = 1.0  # Valor inicial de x
epsilon = 1e-6  # Critério de parada
max_iter = 100  # Número máximo de iterações

# Chamada da função
root, f_root, error, iterations = newton_raphson(f, df, x0, epsilon, max_iter)

# Impressão dos resultados
print("Raiz encontrada:", root)
print("Valor de f(raiz):", f_root)
print("Erro em x:", error)
print("Número de iterações:", iterations)
