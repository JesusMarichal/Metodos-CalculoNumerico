##Instale las Librerias antes de Ejecutar el Codigo
import sympy as sp

def ne(ni, a, b, err, fx, x):
    # Derivadas primera y segunda
    der_exp = sp.diff(fx, x)
    der_exp2 = sp.diff(der_exp, x)

    # Conversiones simbólico → numérico
    f = sp.lambdify(x, fx)
    df = sp.lambdify(x, der_exp)
    d2f = sp.lambdify(x, der_exp2)

    xi = (a + b) / 2  # Punto inicial
    i = 0

    # Validación de convergencia
    if abs(f(xi) * d2f(xi)) / (df(xi))**2 < 1:
        print("Converge ✔️")
    else:
        print("Puede que no converja. Revisa el intervalo.")

    while i < ni:
        print(f'| Iteración {i} | xi = {xi:.6f} | f(xi) = {f(xi):.6f} |')

        # Guardar valor anterior
        xi_ant = xi

        # Actualización con la fórmula de Newton-Raphson
        xi = xi - f(xi) / df(xi)

        # Error relativo
        error = abs(xi - xi_ant) / abs(xi)

        if error <= err:
            break

        i += 1

    print(f'\nResultado aproximado: x = {xi:.6f}, error relativo = {error:.6f}')
    return xi, error

# Ejecución del método
if __name__ == "__main__":
    x = sp.symbols('x')
    fx = sp.exp(x) - 3*x**2
    res = 0.02
    Ni = 100
    a = 0
    b = 1
    result = ne(Ni, a, b, res, fx, x)
