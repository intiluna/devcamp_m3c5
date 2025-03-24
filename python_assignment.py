#1. Cree un bucle For de Python.

# 1.1 Ejemplo de bucle for
print("Ejemplo 1 de bucle for")
for num in range(11):
    print(num)

print("Ejemplo 2 de bucle for")

mi_lista = ["arroz", "pescado","aceite","sal","camarones"]

for ingrediente in mi_lista:
    print(f"Para cocinar el siguiente plato se necesita: {ingrediente}")

print("-" * 50)
#2. Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(n1,n2,n3):
    total = n1 + n2 + n3
    return total

n1,n2,n3 = 1,45,5
test_suma = suma(n1,n2,n3)
print(f"Número a sumar: {n1,n2,n3}") 
print(f"Resultado usando funcion suma:{test_suma}")
print("-" * 50)

#3. Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

mi_lambda = lambda x1,x2,x3: x1 + x2 + x3
print(f"Resultado usando función lambda: {mi_lambda(n1,n2,n3)}")
print("-" * 50)


#4. Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista.
# *Sugerencia, si es necesario, utilice un bucle for in y el operador in.

nombre = 'Enrique'

lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

print("Usando in sin bucle")
if nombre in lista_nombre:
    print(f"El nombre {nombre} esta en la lista")
else:
    print(f"El nombre {nombre} no esta en la lista")

print("- - -" * 10)
print("Usando in con bucle")

for nombre_x in lista_nombre:
    print(nombre_x)
    if nombre_x == nombre:
        print("Tenemos a nuestro nombre target en la lista")
    else:
        print("no match")
    