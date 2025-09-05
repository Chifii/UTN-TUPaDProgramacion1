print("\n")
print("#######################")
print("\n")

# 1) Imprime todos los números enteros desde 0 hasta 100
for i in range(0, 101):
	print(i)
print("\n")
print("#######################")
print("\n")

# 2) Solicita un número entero y determina la cantidad de dígitos
num = int(input("Ingrese un número entero: "))
contador = 0
temp = abs(num)
if temp == 0:
	contador = 1
else:
	while temp > 0:
		temp //= 10
		contador += 1
print("Cantidad de dígitos:", contador)
print("\n")
print("#######################")
print("\n")

# 3) Suma todos los enteros entre dos valores dados por el usuario, excluyendo los extremos
a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))
suma = 0
if a != b:
	menor = a if a < b else b
	mayor = b if a < b else a
	i = menor + 1
	while i < mayor:
		suma += i
		i += 1
print("Suma de los valores entre", a, "y", b, ":", suma)
print("\n")
print("#######################")
print("\n")

# 4) Suma números ingresados por el usuario hasta que ingrese 0
total = 0
n = int(input("Ingrese un número entero (0 para terminar): "))
while n != 0:
	total += n
	n = int(input("Ingrese un número entero (0 para terminar): "))
print("Total acumulado:", total)
print("\n")
print("#######################")
print("\n")

# 5) Juego de adivinar un número aleatorio entre 0 y 9
import random
objetivo = random.randint(0, 9)
intentos = 0
acertado = False
while not acertado:
	guess = int(input("Adivina el número (0-9): "))
	intentos += 1
	if guess == objetivo:
		acertado = True
		print("¡Correcto! El número era", objetivo)
print("Intentos necesarios:", intentos)
print("\n")
print("#######################")
print("\n")

# 6) Imprime todos los números pares entre 0 y 100 en orden decreciente
i = 100
while i >= 0:
	if i % 2 == 0:
		print(i)
	i -= 1
print("\n")
print("#######################")
print("\n")

# 7) Suma todos los números entre 0 y un número positivo indicado por el usuario
entrada = input("Ingrese un número entero positivo (Enter para terminar): ")
if entrada == "":
	print("No se ingresó ningún número. Pasando a la siguiente actividad...")
else:
	n = int(entrada)
	suma = 0
	i = 1
	while i < n:
		suma += i
		i += 1
	print("Suma de los números entre 0 y", n, ":", suma)
print("\n")
print("#######################")
print("\n")

# 8) Ingresar 100 números y contar pares, impares, negativos y positivos
cantidad = 100  # Cambia este valor para probar con menos números
pares = 0
impares = 0
negativos = 0
positivos = 0
contador = 0
while contador < cantidad:
	num = int(input("Ingrese un número entero: "))
	if num % 2 == 0:
		pares += 1
	else:
		impares += 1
	if num < 0:
		negativos += 1
	elif num > 0:
		positivos += 1
	contador += 1
print("Pares:", pares)
print("Impares:", impares)
print("Negativos:", negativos)
print("Positivos:", positivos)
print("\n")
print("#######################")
print("\n")

# 9) Ingresar 100 números y calcular la media
cantidad = 100  # Cambia este valor para probar con menos números
suma = 0
contador = 0
while contador < cantidad:
	num = int(input("Ingrese un número entero: "))
	suma += num
	contador += 1
media = suma / cantidad
print("Media de los valores ingresados:", media)
print("\n")
print("#######################")
print("\n")

# 10) Invierte el orden de los dígitos de un número ingresado
num = int(input("Ingrese un número: "))
invertido = 0
temp = abs(num)
while temp > 0:
	invertido = invertido * 10 + temp % 10
	temp //= 10
print("Número invertido:", invertido)
print("\n")
print("#######################")
print("\n")
