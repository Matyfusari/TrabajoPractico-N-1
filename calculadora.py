from operaciones import suma, resta, division, multiplicacion, factorial

def main():
    operando_a = None
    operando_b = None

    while True:
        print("\nMenú:")
        print("1. Ingresar 1er operando (A={})".format(operando_a if operando_a is not None else "x"))
        print("2. Ingresar 2do operando (B={})".format(operando_b if operando_b is not None else "y"))
        print("3. Calcular todas las operaciones")
        print("4. Informar resultados")
        print("5. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            operando_a = float(input("Ingrese el valor para el primer operando (A): "))
        elif opcion == "2":
            operando_b = float(input("Ingrese el valor para el segundo operando (B): "))
        elif opcion == "3":
            if operando_a is None or operando_b is None:
                print("Por favor ingrese ambos operandos primero.")
            else:
                resultado_suma = suma(operando_a, operando_b)
                resultado_resta = resta(operando_a, operando_b)
                resultado_division = division(operando_a, operando_b)
                resultado_multiplicacion = multiplicacion(operando_a, operando_b)
                resultado_factorial_a = factorial(int(operando_a))
                resultado_factorial_b = factorial(int(operando_b))
                print("Operaciones calculadas.")
        elif opcion == "4":
            if operando_a is None or operando_b is None:
                print("Por favor ingrese ambos operandos primero.")
            else:
                print("Resultados:")
                print("a) El resultado de A+B es:", resultado_suma)
                print("b) El resultado de A-B es:", resultado_resta)
                print("c) El resultado de A/B es:", resultado_division if type(resultado_division) == str else round(resultado_division, 2))
                print("d) El resultado de A*B es:", resultado_multiplicacion)
                print("e) El factorial de A es:", resultado_factorial_a, "y El factorial de B es:", resultado_factorial_b)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor ingrese una opción válida.")

if __name__ == "__main__":
    main()