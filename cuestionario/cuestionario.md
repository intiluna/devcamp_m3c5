# Cuestionario Checkpoint 5
Inti Luna
2025-03-21

## ¿Qué es un condicional?

Una condición es una pregunta sobre una o varias variables, objetos o
estado del sistema o del código. Y una condicional en python es la
evaluación de la condición (o condiciones) y en dependencia de si esta
se cumple se ejecuta un código u otro. Las condiciones logicas son
usadas en python y para ello se usan operadores de comparación. Los
comparadores permiten comparar distintos valores y el resultado es valor
de verdadero o falso (boolean).

Si la expresión de evaluación se cumple, se ejecuta el código después de
“if” (si) y es común pero no es necesario siempre tener una alternativa
de código a ejecutar cuando no se cumple la condición (“else”). En
simples palabras seria: si se cumple la condición, ejecuta esto y si no
se cumple ejecuta este otro código alternativo.

Vamos a ver con unos ejemplos para que se entienda mejor.

Ejemplo 1. Condicionales Imagina que la policia evalua si podemos
conducir en una región que tiene una regulación donde dice que la edad
mínima es de 19 años.

Pregunta: ¿Es la edad mayor de 19 años? Operador a usar: Mayor que que
en python es “\>”

``` python
edad = 20
print(edad)

if edad > 19:
  print("Puede conducir en esta región")
else:
  print("No puede conducir en esta región")
```

    20
    Puede conducir en esta región

Ejemplo 2. Condicionales

Imagina una tienda de zapatos quiere aplicar diferentes descuentos según
el precio del zapato.

En este caso se evaluan dos condiciones y se tiene alternativa para
otros casos:

- Pregunta 1: ¿Es el precio es menor a 50?, aplicando un descuento del
  20%.
- Pregunta 2: ¿Es el precio es menor a 100 (pero mayor o igual a 50)?,
  aplicando un descuento del 10%.
- En todos los otros casos (precio igual o mayor a 100), aplicando un
  descuento del 5%.

``` python
precios_zapatos = [30,60,100]

for precio in precios_zapatos:
  if precio < 50:
    descuento = 20
    print("Zapato económico: ¡tienes un 20% de descuento!")
  elif precio < 100:
      descuento = 10
      print("Zapato de precio medio: te damos un 10% de descuento.")
  else:
      descuento = 5
      print("Zapato premium: aplica un 5% de descuento.")
```

    Zapato económico: ¡tienes un 20% de descuento!
    Zapato de precio medio: te damos un 10% de descuento.
    Zapato premium: aplica un 5% de descuento.

Referencias <https://www.w3schools.com/python/python_conditions.asp>.

## ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

En python existen dos tipos de bucles:

For loops se usan cuando sabemos de antemano cuantas veces vamos a
correr el código en base a un número de veces o cantidad de elementos a
usar en una secuencia.

While loops se usa cuando no sabemos cuantas veces se requiere correr de
antemano el código, cuando se mantenga una condición u ocurra un evento.

En otro lenguajes existe un tercero que es Do-While, es muy similar a
while loop pero asegura que el código se ejecuta al menos una vez.

Vamos a ver algunos ejemplos para entender mejor.

Ejemplo Bucles-1: Para elementos en una lista de valores de
contaminación hacemos un bucle donde se ejecuta una vez por cada
elemento de la lista y en dependencia de valor se imprime si el valor es
alto o normal.

``` python
niveles_contaminacion = [40, 55, 70, 30, 90]
valor_referencia = 50

for nivel in niveles_contaminacion:
    if nivel > valor_referencia:
        print("Nivel alto:", nivel)
    else:
        print("Nivel normal:", nivel)
```

    Nivel normal: 40
    Nivel alto: 55
    Nivel alto: 70
    Nivel normal: 30
    Nivel alto: 90

Ejemplo Bucles-2

Para casos en que no sabemos el número de ejecuciones y depende de una
condición. En este caso, la condición es que mientras el tiempo sea
mayor que 0, vamos a ejecutar el código.

``` python
tiempo_carga = 5

while tiempo_carga > 0:
    print("Cargando... Faltan:", tiempo_carga, "segundos")
    tiempo_carga -= 1

print("Web cargada")
```

    Cargando... Faltan: 5 segundos
    Cargando... Faltan: 4 segundos
    Cargando... Faltan: 3 segundos
    Cargando... Faltan: 2 segundos
    Cargando... Faltan: 1 segundos
    Web cargada

Referencias

<https://medium.com/@heyamit10/for-loop-vs-while-loop-a-comprehensive-guide-for-data-scientists-163b0c11eea0>

<https://realpython.com/python-while-loop/>

## ¿Qué es una lista por comprensión en Python?

Es una manera más compacta de escribir el código que podria estar en for
loop normal. Pueden hacer que el código sea mas simple de leer y
mantener pero tambien pueden hacerlo mas complicado.

Estructura general de lista de comprensión (sin y con condición):

Sin condición: (valores) = \[(expresion) for (valor) in (coleccion)\]
Con condición: (valores) = \[(expresion) for (valor) in (coleccion)
condition\]

Y el equivalente for loop:

Sin condición: (valores) = \[\] for (valor) in (coleccion):
(valores).append( (expresion) ) Con condición: (valores) = \[\] for
(valor) in (coleccion): if (condicion): (valores).append(expresion)

Ahora vamos a ver un ejemplo donde sumamos 1 a cada valor:

``` python
suma_uno = [x + 1 for x in range(5)]
print(f"antes de aplicar:{list(range(5))}")
print(f"despues:{suma_uno}")

suma_uno_normal =[]
for x in range(5):
  x_nuevo = x + 1
  suma_uno_normal.append(x_nuevo)

print(f"resultado usando for-loop normal:{suma_uno_normal}")
```

    antes de aplicar:[0, 1, 2, 3, 4]
    despues:[1, 2, 3, 4, 5]
    resultado usando for-loop normal:[1, 2, 3, 4, 5]

Otro ejemplo de filtrar:

``` python
valores = [10,15,5,6,89,34]
umbral = 20
valores_filtrados = [x for x in valores if x > umbral]
print(f"valores iniciales:{valores}")
print(f"despues de filtrar:{valores_filtrados}")

valores_filtrados_normal =[]
for x in valores:
  if x > umbral:
    valores_filtrados_normal.append(x)

print(f"resultado usando for-loop normal:{valores_filtrados_normal}")
```

    valores iniciales:[10, 15, 5, 6, 89, 34]
    despues de filtrar:[89, 34]
    resultado usando for-loop normal:[89, 34]

Si la lista de comprensión se hace muy larga, se propone usar un formato
que facilite la lectura como el que se muestra donde se separa en varias
lineas:

![Formato propuesto para list
comprehension](images/format_list_comprehension.png)

Por último, hay que tener en cuenta que el código va a ser revisado por
otros desarrolladores y si la list comprehension no es familiar para
ellos hay que evitarlas. Adicionalmente, Si hay nested for loops, no se
recomienda hacer nested list comprehension, ya que dificulta la lectura
y pueden causar confusión.

Referencias:
<https://realpython.com/videos/writing-your-first-list-comprehension/>

## ¿Qué es un argumento en Python?

Las funciones pueden tener datos o valores que les son suministrados
llamados argumentos, se colocan dentro del parentesis y la función los
utiliza de alguna manera.

Tipos de argumento:

- **Argumentos posicionales** son aquellos que se pasan en el mismo
  orden en que la función fueron definidos.

``` python
def saludar(nombre, pueblo):
    print(f"Hola {nombre} de {pueblo}")


saludar("Ana", "Gernika")
```

    Hola Ana de Gernika

- **Argumentos con nombre (keywords)** tienen la ventaja que no importa
  el orden porque se pasa el valor con el nombre del argumento.

``` python
def saludar(nombre, pueblo, hobby):
    print(f"Hola {nombre} de {pueblo}. Entiendo que tu hobby es {hobby}")


saludar(nombre ="Ana", hobby="nadar", pueblo="Gernika")
```

    Hola Ana de Gernika. Entiendo que tu hobby es nadar

- **Argumentos con valores por defecto o predeterminados** que permite
  llamar a la función sin el argumento predeterminado.

``` python
def saludar(nombre, pueblo, hobby="programar"):
    print(f"Hola {nombre} de {pueblo}. Entiendo que tu hobby es {hobby}")


saludar(nombre ="Ana",  pueblo="Gernika")
```

    Hola Ana de Gernika. Entiendo que tu hobby es programar

- **Argumentos variables usando \*args** cuando se puede pasar un número
  arbitrario de argumentos y puede ser diferentes en cada llamada. Por
  convención se usa \*args pero puede ser cualquiera nombre como en el
  siguiente ejemplo de peso de peces.

``` python
def total_peso(*peces):
    total = sum(peces)
    print("El peso total de los peces es:", total, "kg")


total_peso(1.5,2,3)
```

    El peso total de los peces es: 6.5 kg

- **Argumentos variables con nombre usando \*\*kwargs** cuando se puede
  pasar un número arbitrario de argumentos con nombre.

``` python
def reporta_ejercicios(**kwargs):
    for ejercicio, medida in kwargs.items():
      print(f"Actividad: {ejercicio}, Logro: {medida}")


reporta_ejercicios(nadar="1.5 km", correr = "3 veces al dia", saltar = "10 metros")
print("--------------------------")
reporta_ejercicios(bicicleta="20 km", saltar = "30 metros")
```

    Actividad: nadar, Logro: 1.5 km
    Actividad: correr, Logro: 3 veces al dia
    Actividad: saltar, Logro: 10 metros
    --------------------------
    Actividad: bicicleta, Logro: 20 km
    Actividad: saltar, Logro: 30 metros

Referencias:

<https://www.w3schools.com/python/gloss_python_function_arguments.asp>

<https://www.w3schools.com/python/gloss_python_function_arbitrary_arguments.asp>

## ¿Qué es una función Lambda en Python?

## ¿Qué es un paquete pip?
