# TP-01: Estructuras Secuenciales
# Nombre: [Esteban]
# Apellido: [Ferreyra]

import math

print("="*50)
print("TP-01: ESTRUCTURAS SECUENCIALES")
print("="*50)

# 1) Programa que imprime "Hola Mundo!"
print("\n1) Mensaje Hola Mundo:")
print("Hola Mundo!")

# 2) Programa que pide el nombre y saluda
print("\n2) Saludo personalizado:")
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Programa que pide datos personales e imprime una oración
print("\n3) Datos personales:")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

# 4) Programa que calcula área y perímetro de un círculo
print("\n4) Área y perímetro de un círculo:")
radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")

# 5) Programa que convierte segundos a horas
print("\n5) Conversión de segundos a horas:")
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas")

# 6) Programa que muestra la tabla de multiplicar
print("\n6) Tabla de multiplicar:")
numero = int(input("Ingrese un número: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# 7) Programa que opera con dos números
print("\n7) Operaciones con dos números:")
num1 = float(input("Ingrese el primer número (distinto de 0): "))
num2 = float(input("Ingrese el segundo número (distinto de 0): "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} × {num2} = {multiplicacion}")
print(f"División: {num1} ÷ {num2} = {division:.2f}")

# 8) Programa que calcula el IMC
print("\n8) Cálculo del Índice de Masa Corporal (IMC):")
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
imc = peso / (altura ** 2)
print(f"Su IMC es: {imc:.2f}")

# 9) Programa que convierte Celsius a Fahrenheit
print("\n9) Conversión de Celsius a Fahrenheit:")
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# 10) Programa que calcula el promedio de 3 números
print("\n10) Promedio de 3 números:")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")

print("\n" + "="*50)
print("FIN DEL PROGRAMA")
print("="*50)