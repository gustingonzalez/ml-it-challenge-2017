#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
from operator import itemgetter


# Verifica si un número es primo.
def is_prime(n):

    # Se evita comprobación contra uno y el mismo número.
    for x in range(2, n):
        # Si el resto de dividir el nro. por el mismo y 1 es 0...
        if(n % x == 0):
            # No es primo.
            return False
    return True


# Retorna el conteo de los intervalos a los que se encuentran los índices
def get_intervals(indexes):
    intervals = collections.Counter()

    # Verificación de distancias.
    for x in range(0, len(indexes)):
        val1 = indexes[x]
        # Se comprueba distancia contra cada sub-elemento, desde el elemento
        # actual, ya que todas las distancias son candidatas.
        for i in range(x+1, len(indexes)-1):
            val2 = indexes[i+1]

            intervals[val2-val1] += 1

    return intervals


f = open("level13.txt")

numbers = []

for x in f:
    numbers.append(int(x))

f.close()

primes = set(n for n in numbers if is_prime(n) and n != 0 and n != 1)

# Verificación de intervalos de primos.
candidates = []

for n in primes:
    indexes = []

    # Append de indexes.
    for i in range(0, len(numbers)):
        if(numbers[i] == n):
            indexes.append(i)

    # Se toma el top 10 por probabilidad de error inherente.
    intervals = get_intervals(indexes).most_common(10)

    for i in range(0, len(intervals)):
        # Núm, distancia, freq.
        candidates.append([n, intervals[i][0], intervals[i][1]])

candidates.sort(key=lambda x: x[2])

# Se filtran los candidatos a los 10 primeros.
for c in candidates[0:10]:
    print "Prime number:", c[0], " - Distance:", c[1], "- Freq:", c[2]
    print "Final number:", c[0] * c[1]
    print ""
