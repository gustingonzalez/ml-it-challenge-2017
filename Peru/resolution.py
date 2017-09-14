#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Verifica si un número es primo.
def is_prime(n):

    # Se evita comprobación contra uno y el mismo número.
    for x in range(2, n):
        # Si el resto de dividir el nro. por el mismo y 1 es 0...
        if(n%x == 0):
            # No es primo.
            return False
    return True


# Lectura de dígitos de pi
f = open("100000_decimals_pi.txt")

pi = ""
for line in f:
    pi += line[:-1]
f.close()

size = 7
place = 7
finded = 0

for i in range(0, len(pi)):
    number = pi[i:i+size]

    # Si es capicua.
    if number == number[::-1]:

        if(is_prime(int(number))):
            place -= 1
            # Si es el número en el puesto especificado.
            if place == 0:
                finded = int(number)
                break

print finded
