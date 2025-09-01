print("\n")
print("#######################")
print("\n")

# 1) Programa que solicita la edad y dice si es mayor de edad
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
print("\n")
print("#######################")
print("\n")

# 2) Programa que solicita la nota y dice si está aprobado o desaprobado
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
print("\n")
print("#######################")
print("\n")

# 3) Programa que permite ingresar solo números pares
n = int(input("Ingrese un numero: "))
if n % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
print("\n")
print("#######################")
print("\n")

# 4) Programa que clasifica la edad en categorías
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
print("\n")
print("#######################")
print("\n")

# 5) Programa que valida longitud de contraseña (8 a 14)
pwd = input("Ingrese una contraseña: ")
if len(pwd) >= 8 and len(pwd) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
print("\n")
print("#######################")
print("\n")

# 6) Programa que evalúa sesgo estadístico con media, mediana y moda
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
m = mean(numeros_aleatorios)
md = median(numeros_aleatorios)
mo = mode(numeros_aleatorios)

if m > md and md > mo:
    print("Sesgo positivo o a la derecha")
elif m < md and md < mo:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")
print("\n")
print("#######################")
print("\n")

# 7) Programa que añade '!' si la palabra termina en vocal
s = input("Ingrese una palabra o frase: ")
if s.endswith(("a","e","i","o","u","A","E","I","O","U")):
    s = s + "!"
print(s)
print("\n")
print("#######################")
print("\n")

# 8) Programa que transforma nombre según opción elegida
nombre = input("Ingrese su nombre: ")
op = int(input("Ingrese 1 (MAY), 2 (min), 3 (Titulo): "))

if op == 1:
    print(nombre.upper())
elif op == 2:
    print(nombre.lower())
else:
    print(nombre.title())
print("\n")
print("#######################")
print("\n")

# 9) Programa que clasifica la magnitud de un terremoto según la escala de Richter
mag = float(input("Ingrese la magnitud del terremoto: "))

if mag < 3:
    print("Muy leve")
elif mag >= 3 and mag < 4:
    print("Leve")
elif mag >= 4 and mag < 5:
    print("Moderado")
elif mag >= 5 and mag < 6:
    print("Fuerte")
elif mag >= 6 and mag < 7:
    print("Muy Fuerte")
else:
    print("Extremo")
print("\n")
print("#######################")
print("\n")

# 10) Programa que determina estación del año según hemisferio, mes y día
hem = input("Hemisferio (N/S): ").upper()
mes = int(input("Mes (1-12): "))
dia = int(input("Dia (1-31): "))

def geq(a,b):
    return a[0] > b[0] or (a[0] == b[0] and a[1] >= b[1])
def leq(a,b):
    return a[0] < b[0] or (a[0] == b[0] and a[1] <= b[1])

fecha = (mes, dia)
print("\n")
print("#######################")
print("\n")

# Rangos hemisferio norte
inv_n = ( (12,21), (3,20) )
pri_n = ( (3,21),  (6,20) )
ver_n = ( (6,21),  (9,20) )
oto_n = ( (9,21), (12,20) )

def en_rango(f, r):
    ini, fin = r
    if geq(fin, ini):
        return geq(f, ini) and leq(f, fin)
    else:
        return geq(f, ini) or leq(f, fin)

if hem == "N":
    if en_rango(fecha, inv_n):
        print("Invierno")
    elif en_rango(fecha, pri_n):
        print("Primavera")
    elif en_rango(fecha, ver_n):
        print("Verano")
    else:
        print("Otoño")
else:
    if en_rango(fecha, inv_n):
        print("Verano")
    elif en_rango(fecha, pri_n):
        print("Otoño")
    elif en_rango(fecha, ver_n):
        print("Invierno")
    else:
        print("Primavera")
print("\n")
print("#######################")
print("\n")