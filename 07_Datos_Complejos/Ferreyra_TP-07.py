import string

print("\n")
print("#######################")
print("\n")

# Actividad 1: Agregar frutas con precios
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print("Diccionario actualizado:", precios_frutas)
print("\n")
print("#######################")
print("\n")

# Actividad 2: Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print("Diccionario actualizado:", precios_frutas)
print("\n")
print("#######################")
print("\n")

# Actividad 3: Lista solo de frutas (claves)
frutas = list(precios_frutas.keys())
print("Frutas:", frutas)
print("\n")
print("#######################")
print("\n")

# Actividad 4: Agenda telefónica simple
agenda = {}
for i in range(1, 6):
    nombre = input(f"Nombre #{i}: ").strip()
    numero = input(f"Número de {nombre}: ").strip()
    agenda[nombre] = numero
buscar = input("Ingresá un nombre a consultar: ").strip()
if buscar in agenda:
    print(f"Número de {buscar}: {agenda[buscar]}")
else:
    print("Nombre no encontrado.")
print("\n")
print("#######################")
print("\n")

# Actividad 5: Palabras únicas y conteo por palabra
def normalizar_palabra(p):
    return p.lower().strip(string.punctuation)

frase = input("Ingresá una frase: ").strip()
palabras = [normalizar_palabra(p) for p in frase.split() if normalizar_palabra(p)]
unicas = set(palabras)
conteo = {}
for p in palabras:
    conteo[p] = conteo.get(p, 0) + 1
print("Palabras únicas:", unicas)
print("Conteo:", conteo)
print("\n")
print("#######################")
print("\n")

# Actividad 6: Promedio de 3 alumnos con tupla de 3 notas
def leer_notas_tuple():
    while True:
        try:
            partes = input("Ingresá 3 notas separadas por espacio: ").strip().split()
            if len(partes) != 3:
                print("Debés ingresar exactamente 3 notas.")
                continue
            notas = tuple(float(x.replace(",", ".")) for x in partes)
            return notas
        except ValueError:
            print("Notas inválidas. Intentá de nuevo.")

alumnos = {}
for i in range(1, 4):
    nombre = input(f"Nombre del alumno #{i}: ").strip()
    notas = leer_notas_tuple()
    alumnos[nombre] = notas
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: notas={notas} | promedio={promedio:.2f}")
print("\n")
print("#######################")
print("\n")

# Actividad 7: Aprobados Parcial 1 y Parcial 2 (conjuntos)
def leer_set_enteros(msg):
    while True:
        linea = input(msg).strip()
        if not linea:
            print("Ingresá al menos un número.")
            continue
        try:
            return set(int(x) for x in linea.replace(",", " ").split())
        except ValueError:
            print("Entrada inválida. Usá enteros separados por espacio o coma.")

p1 = leer_set_enteros("IDs aprobados Parcial 1: ")
p2 = leer_set_enteros("IDs aprobados Parcial 2: ")
ambos = p1 & p2
solo_uno = p1 ^ p2
al_menos_uno = p1 | p2
print("Aprobaron ambos:", sorted(ambos))
print("Aprobaron solo uno:", sorted(solo_uno))
print("Aprobaron al menos uno:", sorted(al_menos_uno))
print("\n")
print("#######################")
print("\n")

# Actividad 8: Stock por producto
stock = {}
while True:
    accion = input("Acciones: [C]onsultar / [A]gregar unidades / [N]uevo producto / [S]alir: ").strip().lower()
    if accion == "s":
        break
    if accion == "c":
        prod = input("Producto a consultar: ").strip()
        if prod in stock:
            print(f"Stock de {prod}: {stock[prod]}")
        else:
            print("No existe. Podés crearlo con 'N'.")
    elif accion == "a":
        prod = input("Producto existente: ").strip()
        if prod in stock:
            try:
                cant = int(input("Unidades a agregar: ").strip())
                stock[prod] += cant
                print(f"Nuevo stock de {prod}: {stock[prod]}")
            except ValueError:
                print("Cantidad inválida.")
        else:
            print("El producto no existe.")
    elif accion == "n":
        prod = input("Nombre del nuevo producto: ").strip()
        if prod in stock:
            print("Ya existe. Usá 'A' para sumar.")
        else:
            try:
                cant = int(input("Stock inicial: ").strip())
                stock[prod] = cant
                print(f"Creado {prod} con stock {cant}.")
            except ValueError:
                print("Cantidad inválida.")
    else:
        print("Opción inválida.")
print("Stock final:", stock)
print("\n")
print("#######################")
print("\n")

# Actividad 9: Agenda de eventos con clave (día, hora)
agenda = {
    ("Lunes", "09:00"): "Daily",
    ("Miércoles", "15:00"): "Entrevista",
    ("Viernes", "10:00"): "Revisión semanal",
}
dia = input("Consultá día (ej: Lunes): ").strip().title()
hora = input("Consultá hora (HH:MM): ").strip()
evento = agenda.get((dia, hora))
if evento:
    print(f"En {dia} a las {hora}: {evento}")
else:
    print("No hay actividad registrada.")
print("\n")
print("#######################")
print("\n")

# Actividad 10: Invertir diccionario País -> Capital a Capital -> País
print("Cargá pares 'pais:capital'. Enter vacío para terminar.")
pais_cap = {}
while True:
    linea = input("Par (pais:capital): ").strip()
    if not linea:
        break
    if ":" not in linea:
        print("Formato inválido. Usá 'pais:capital'.")
        continue
    pais, capital = [x.strip() for x in linea.split(":", 1)]
    if not pais or not capital:
        print("Valores vacíos no permitidos.")
        continue
    pais_cap[pais] = capital
capital_pais = {capital: pais for pais, capital in pais_cap.items()}
print("Diccionario invertido:", capital_pais)
print("\n")
print("#######################")
print("\n")