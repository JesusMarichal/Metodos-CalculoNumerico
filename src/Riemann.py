
##IMPORTANTE IMPORTAR TODAS LAS LIBRERIAS ANTES DE CORRER
import sympy as sp
import math
def riemann_integral(f, a, b, n, xi):
    h = (b - a) / n
    x = a
    total = 0
    exp = sp.lambdify(xi, f)
    for _ in range(n):
        total += exp(x) * h
        x += h
    return total
if __name__ == "__main__":
    x=sp.symbols('x')
    f= x**2*sp.cos(x**3-1)
    a=math.pi/2
    b=0
    n=4
    result=riemann_integral(f,a,b,n,x)
    print(" ")
    print(f'El Resultado es: {result}')