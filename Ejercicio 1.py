# Ejercicio 1: Saludo y Captura de Nombre
nombre = input("Ingrese su nombre: ")
print(f"Hola, {nombre}!")

# Ejercicio 2: Operaciones Matemáticas
numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese otro número: "))

suma = numero1 + numero2
resta = numero1 - numero2
producto = numero1 * numero2
division = numero1 / numero2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Producto: {producto}")
print(f"División: {division}")

# Ejercicio 3: Lista y Bucle
numeros = [1, 2, 3, 4, 5]

print("Elementos de la lista:")
for num in numeros:
    print(num)

# Ejercicio 4: Función para Calcular el Cuadrado
def calcular_cuadrado(x):
    return x ** 2

numero = float(input("Ingrese un número para calcular su cuadrado: "))
resultado = calcular_cuadrado(numero)
print(f"El cuadrado de {numero} es {resultado}")