import math

def f(x):
    return math.cos(x)**3 - math.sin(x)

def secant_method(f, x0, x1, tolerance, max_iterations):
    x2 = 0
    iteration = 0

    while abs(x1 - x0) > tolerance and iteration < max_iterations:
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
        iteration += 1

    f_x = f(x2)
    average_x = (x0 + x1) / 2
    error_x = abs(x1 - x0)

    return {
        'root': x2,
        'f_x': f_x,
        'average_x': average_x,
        'error_x': error_x,
        'iterations': iteration
    }

# Exemplo de uso
x0 = 0.5  # Valor inicial x0
x1 = 1.0  # Valor inicial x1
tolerance = 1e-6  # Tolerância
max_iterations = 100  # Número máximo de iterações

result = secant_method(f, x0, x1, tolerance, max_iterations)
print("Raiz da função:", result['root'])
print("f(x) na raiz:", result['f_x'])
print("Média amostral:", result['average_x'])
print("Erro em x:", result['error_x'])
print("Número de iterações:", result['iterations'])
