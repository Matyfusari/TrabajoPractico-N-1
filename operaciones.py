def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def division(a, b):
    if b == 0:
        return "No es posible dividir por cero"
    else:
        return a / b

def multiplicacion(a, b):
    return a * b

def factorial(n):
    """Calcula el factorial de un número."""
    if n < 0:
        raise ValueError("Factorial no está definido para números negativos")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result