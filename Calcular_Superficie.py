def calcular_superficie(lado1, lado2):
    return lado1 * lado2

lado1_rectangulo1 = float(input("Ingrese el primer lado del primer rectángulo: "))
lado2_rectangulo1 = float(input("Ingrese el segundo lado del primer rectángulo: "))

lado1_rectangulo2 = float(input("Ingrese el primer lado del segundo rectángulo: "))
lado2_rectangulo2 = float(input("Ingrese el segundo lado del segundo rectángulo: "))

superficie_rectangulo1 = calcular_superficie(lado1_rectangulo1, lado2_rectangulo1)
superficie_rectangulo2 = calcular_superficie(lado1_rectangulo2, lado2_rectangulo2)

if superficie_rectangulo1 > superficie_rectangulo2:
    print("El primer rectángulo tiene una superficie mayor.")
elif superficie_rectangulo2 > superficie_rectangulo1:
    print("El segundo rectángulo tiene una superficie mayor.")
else:
    print("Ambos rectángulos tienen la misma superficie.")
