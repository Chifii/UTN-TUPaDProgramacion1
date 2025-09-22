import random

print("\n")
print("#######################")
print("\n")

# 1) Lista de notas de 10 estudiantes
notas = [random.randint(1, 10) for _ in range(10)]
print('Notas de los estudiantes:')
for nota in notas:
    print(nota)
promedio = sum(notas) / len(notas)
print(f'Promedio: {promedio:.2f}')
print(f'Nota más alta: {max(notas)}')
print(f'Nota más baja: {min(notas)}')
print("\n")
print("#######################")
print("\n")

# 2) Cargar 5 productos y eliminar uno
productos = []
for i in range(5):
    prod = input(f'Ingrese el nombre del producto {i+1}: ')
    productos.append(prod)
print('Lista ordenada:')
for prod in sorted(productos):
    print(prod)
eliminar = input('¿Qué producto desea eliminar?: ')
if eliminar in productos:
    productos.remove(eliminar)
    print('Lista actualizada:')
    for prod in productos:
        print(prod)
else:
    print('Producto no encontrado.')
print("\n")
print("#######################")
print("\n")

# 3) Lista de 15 números aleatorios, pares e impares
numeros = [random.randint(1, 100) for _ in range(15)]
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]
print('Números generados:')
for n in numeros:
    print(n)
print(f'Cantidad de pares: {len(pares)}')
print(f'Cantidad de impares: {len(impares)}')
print("\n")
print("#######################")
print("\n")

# 4) Eliminar repetidos de una lista
lista_repetidos = [1,2,2,3,4,4,5,1,6,7,7,8]
lista_sin_repetidos = list(set(lista_repetidos))
print('Lista sin repetidos:')
for n in lista_sin_repetidos:
    print(n)
print("\n")
print("#######################")
print("\n")

# 5) Lista de estudiantes presentes
estudiantes = ['Ana', 'Luis', 'Marta', 'Juan', 'Sofía', 'Pedro', 'Lucía', 'Carlos']
accion = input('¿Desea agregar (A) o eliminar (E) un estudiante?: ').upper()
if accion == 'A':
    nuevo = input('Nombre del nuevo estudiante: ')
    estudiantes.append(nuevo)
elif accion == 'E':
    eliminar = input('Nombre del estudiante a eliminar: ')
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
    else:
        print('Estudiante no encontrado.')
print('Lista final de estudiantes:')
for est in estudiantes:
    print(est)
print("\n")
print("#######################")
print("\n")

# 6) Rotar lista de 7 números a la derecha
numeros_rotar = [1,2,3,4,5,6,7]
print('Lista original:')
for n in numeros_rotar:
    print(n)
numeros_rotar = [numeros_rotar[-1]] + numeros_rotar[:-1]
print('Lista rotada:')
for n in numeros_rotar:
    print(n)
print("\n")
print("#######################")
print("\n")

# 7) Matriz 7x2 de temperaturas mínimas y máximas
temperaturas = [[random.randint(5,15), random.randint(16,30)] for _ in range(7)]
minimas = [dia[0] for dia in temperaturas]
maximas = [dia[1] for dia in temperaturas]
prom_min = sum(minimas)/len(minimas)
prom_max = sum(maximas)/len(maximas)
amplitudes = [maximas[i]-minimas[i] for i in range(7)]
dia_max_amp = amplitudes.index(max(amplitudes)) + 1
print('Temperaturas (mín, máx) por día:')
for i, dia in enumerate(temperaturas):
    print(f'Día {i+1}: {dia}')
print(f'Promedio mínimas: {prom_min:.2f}')
print(f'Promedio máximas: {prom_max:.2f}')
print(f'Día con mayor amplitud térmica: Día {dia_max_amp}')
print("\n")
print("#######################")
print("\n")

# 8) Matriz de notas de 5 estudiantes en 3 materias
notas_matriz = [[random.randint(1,10) for _ in range(3)] for _ in range(5)]
print('Notas de estudiantes:')
for i, fila in enumerate(notas_matriz):
    print(f'Estudiante {i+1}: {fila}')
    print(f'Promedio estudiante {i+1}: {sum(fila)/len(fila):.2f}')
prom_materias = [sum([notas_matriz[i][j] for i in range(5)])/5 for j in range(3)]
for j, prom in enumerate(prom_materias):
    print(f'Promedio materia {j+1}: {prom:.2f}')
print("\n")
print("#######################")
print("\n")

# 9) Tablero de Ta-Te-Ti
print('Tablero Ta-Te-Ti:')
tablero = [['-' for _ in range(3)] for _ in range(3)]
for fila in tablero:
    print(' '.join(fila))
for turno in range(5):
    jugador = 'X' if turno % 2 == 0 else 'O'
    print(f'Turno de {jugador}')
    fila = int(input('Fila (0-2): '))
    col = int(input('Columna (0-2): '))
    if tablero[fila][col] == '-':
        tablero[fila][col] = jugador
    else:
        print('Casilla ocupada, pierdes turno.')
    for fila_print in tablero:
        print(' '.join(fila_print))
print("\n")
print("#######################")
print("\n")

# 10) Matriz de ventas de 4 productos en 7 días
ventas = [[random.randint(0,20) for _ in range(7)] for _ in range(4)]
print('Ventas por producto y día:')
for i, prod in enumerate(ventas):
    print(f'Producto {i+1}: {prod}')
total_prod = [sum(prod) for prod in ventas]
for i, total in enumerate(total_prod):
    print(f'Total vendido Producto {i+1}: {total}')
total_dia = [sum([ventas[p][d] for p in range(4)]) for d in range(7)]
dia_max = total_dia.index(max(total_dia)) + 1
print(f'Día con mayores ventas totales: Día {dia_max}')
prod_max = total_prod.index(max(total_prod)) + 1
print(f'Producto más vendido en la semana: Producto {prod_max}')
print("\n")
print("#######################")
print("\n")