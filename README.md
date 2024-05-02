## operador morsa

¡Claro! El operador morsa (también conocido como operador walrus) fue introducido en Python 3.8 y se representa con dos puntos seguidos de un igual (:=). Su nombre proviene de su similitud con los ojos y colmillos de una morsa .

Este operador tiene una característica interesante: permite asignar y devolver una variable en la misma sentencia. Antes de su introducción, no era posible hacer esto en Python. Veamos algunos ejemplos para entender mejor su uso:

## Entrada de números en una lista:
Supongamos que queremos que un usuario introduzca números en una lista a través de un input, y que para dejar de incluirlos tenga que presionar el número 0. Sin el operador morsa, podríamos hacerlo así:

> Ejemplo :

''' python
lista = []
while True:
    numero = int(input('Añade número: '))
    if numero == 0:
        break
    lista.append(numero)
print(lista)
'''

## Con el operador morsa, podemos reducir el código a lo siguiente:

'''python
lista = []
while (numero := int(input('Añade número: '))) != 0:
    lista.append(numero)
print(lista)
'''
Ambos códigos producirán la misma lista [4, 3, 6, 2, 9] para las siguientes entradas de datos: 4, 3, 6, 2, 9, 0.
## Asignaciones múltiples en una línea:
 También podemos hacer varias asignaciones en la misma línea de código.

 > Ejemplo :
'''python

 (n_cuadrado := (n := 10) * n)
print(n, n_cuadrado)  # Devuelve 10 y 100
'''
### En resumen, el uso del operador morsa debe limitarse a los casos en los que la legibilidad del código mejore. Sin embargo, ten en cuenta que no es compatible con versiones de Python anteriores a la 3.81234.