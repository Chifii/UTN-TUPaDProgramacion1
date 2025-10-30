print("\n")
print("#######################")
print("\n")

# Ejercicio 1: Factorial recursivo
def factorial(n):
    """Función recursiva que calcula el factorial de un número"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("EJERCICIO 1: Factorial recursivo")
try:
    numero = int(input("Ingrese un número para calcular factoriales de 1 hasta ese número: "))
    if numero >= 1:
        print(f"Factoriales de 1 hasta {numero}:")
        for i in range(1, numero + 1):
            resultado = factorial(i)
            print(f"{i}! = {resultado}")
    else:
        print("Por favor ingrese un número mayor o igual a 1")
except ValueError:
    print("Por favor ingrese un número entero válido")

print("\n")
print("#######################")
print("\n")

# Ejercicio 2: Serie de Fibonacci
def fibonacci(n):
    """Función recursiva que calcula el valor de Fibonacci en la posición n"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("EJERCICIO 2: Serie de Fibonacci")
try:
    posicion = int(input("Ingrese la posición hasta donde mostrar la serie de Fibonacci: "))
    if posicion >= 0:
        print(f"Serie de Fibonacci hasta la posición {posicion}:")
        for i in range(posicion + 1):
            valor = fibonacci(i)
            print(f"F({i}) = {valor}")
    else:
        print("Por favor ingrese un número mayor o igual a 0")
except ValueError:
    print("Por favor ingrese un número entero válido")

print("\n")
print("#######################")
print("\n")

# Ejercicio 3: Potencia recursiva
def potencia(base, exponente):
    """Función recursiva que calcula base^exponente"""
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base
    else:
        return base * potencia(base, exponente - 1)

print("EJERCICIO 3: Potencia recursiva")
try:
    base = float(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente (entero no negativo): "))
    if exponente >= 0:
        resultado = potencia(base, exponente)
        print(f"{base}^{exponente} = {resultado}")
    else:
        print("Por favor ingrese un exponente no negativo")
except ValueError:
    print("Por favor ingrese valores numéricos válidos")

print("\n")
print("#######################")
print("\n")

# Ejercicio 4: Conversión decimal a binario
def decimal_a_binario(n):
    """Función recursiva que convierte un número decimal a binario"""
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

print("EJERCICIO 4: Conversión decimal a binario")
try:
    numero = int(input("Ingrese un número entero positivo para convertir a binario: "))
    if numero >= 0:
        binario = decimal_a_binario(numero)
        print(f"El número {numero} en binario es: {binario}")
    else:
        print("Por favor ingrese un número entero positivo")
except ValueError:
    print("Por favor ingrese un número entero válido")

print("\n")
print("#######################")
print("\n")

# Ejercicio 5: Verificar palíndromo
def es_palindromo(palabra):
    """Función recursiva que verifica si una palabra es palíndromo"""
    # Convertir a minúsculas para comparación
    palabra = palabra.lower()
    
    # Caso base: si la palabra tiene 0 o 1 caracteres, es palíndromo
    if len(palabra) <= 1:
        return True
    
    # Si el primer y último carácter son diferentes, no es palíndromo
    if palabra[0] != palabra[-1]:
        return False
    
    # Verificar recursivamente la palabra sin el primer y último carácter
    return es_palindromo(palabra[1:-1])

print("EJERCICIO 5: Verificar palíndromo")
palabra = input("Ingrese una palabra (sin espacios ni tildes) para verificar si es palíndromo: ")
if es_palindromo(palabra):
    print(f"'{palabra}' SÍ es un palíndromo")
else:
    print(f"'{palabra}' NO es un palíndromo")

print("\n")
print("#######################")
print("\n")

# Ejercicio 6: Suma de dígitos
def suma_digitos(n):
    """Función recursiva que suma todos los dígitos de un número"""
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

print("EJERCICIO 6: Suma de dígitos")
try:
    numero = int(input("Ingrese un número entero positivo para sumar sus dígitos: "))
    if numero >= 0:
        resultado = suma_digitos(numero)
        print(f"La suma de los dígitos de {numero} es: {resultado}")
    else:
        print("Por favor ingrese un número entero positivo")
except ValueError:
    print("Por favor ingrese un número entero válido")

print("\n")
print("#######################")
print("\n")

# Ejercicio 7: Contar bloques de pirámide
def contar_bloques(n):
    """Función recursiva que cuenta el total de bloques en una pirámide"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

print("EJERCICIO 7: Contar bloques de pirámide")
try:
    niveles = int(input("Ingrese el número de bloques en el nivel más bajo de la pirámide: "))
    if niveles > 0:
        total_bloques = contar_bloques(niveles)
        print(f"Para una pirámide con {niveles} bloques en la base se necesitan {total_bloques} bloques en total")
        
        # Mostrar la estructura de la pirámide
        print("Estructura de la pirámide:")
        for i in range(niveles, 0, -1):
            print(f"Nivel {niveles - i + 1}: {i} bloques")
    else:
        print("Por favor ingrese un número positivo")
except ValueError:
    print("Por favor ingrese un número entero válido")

print("\n")
print("#######################")
print("\n")

# Ejercicio 8: Contar apariciones de un dígito
def contar_digito(numero, digito):
    """Función recursiva que cuenta cuántas veces aparece un dígito en un número"""
    if numero == 0:
        return 1 if digito == 0 else 0
    
    ultimo_digito = numero % 10
    resto_numero = numero // 10
    
    if ultimo_digito == digito:
        return 1 + contar_digito(resto_numero, digito)
    else:
        return contar_digito(resto_numero, digito)

print("EJERCICIO 8: Contar apariciones de un dígito")
try:
    numero = int(input("Ingrese un número entero positivo: "))
    digito = int(input("Ingrese el dígito a contar (0-9): "))
    
    if numero >= 0 and 0 <= digito <= 9:
        apariciones = contar_digito(numero, digito)
        print(f"El dígito {digito} aparece {apariciones} veces en el número {numero}")
    else:
        print("Por favor ingrese un número positivo y un dígito entre 0 y 9")
except ValueError:
    print("Por favor ingrese valores numéricos válidos")

print("\n")
print("#######################")
print("\n")
