import sympy as sp

def trapecio(f, a, b, n, x):
    h = (b - a) / n
    f_eval = sp.lambdify(x, f, 'sympy')  #sympy para evitar errores

    suma = 0.5 * (f_eval(a) + f_eval(b))  #extremos
    xi = a + h

    for _ in range(1, n):
        suma += f_eval(xi)
        xi += h

    return suma * h

# Ejecución main
if __name__ == "__main__":
    x = sp.symbols('x')
    f = x**2 * sp.cos(x**3 - 1)  # expresión simbólica
    a = 0
    b = sp.pi / 2
    n = 4  # intervalos, Cuanto mayor sea n, más precisión tendrá

    resultado = trapecio(f, a, b, n, x)
    print(f"Resultado por Metodo del Trapecio: {resultado:.6f}")

