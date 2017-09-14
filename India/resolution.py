#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 03/09/17

capacity = 25185
oranges = 109
bananas = 17188

max_filled = 0

for x in range(0, capacity+1):
    fill = (x*oranges)/2

    # Si el fill supera la capacidad, se termina el ciclo, pues las
    # sucesivas comprobaciones serían innecesarias.
    if fill > capacity:
        break

    new_fill = fill

    for y in range(0, capacity+1):
        fill = (x*oranges+y*bananas)/2

        # Si el fill supera la capacidad, se termina el ciclo, pues las
        # sucesivas comprobaciones serían innecesarias.
        if fill > capacity:
            break

        new_fill = fill

        for j in range(0, capacity+1):
            fill = (x*oranges+y*bananas)/2 + j*oranges

            # Si el fill supera la capacidad, se termina el ciclo, pues las
            # sucesivas comprobaciones serían innecesarias.
            if fill > capacity:
                break

            new_fill = fill

            for k in range(0, capacity+1):
                fill = (x*oranges+y*bananas)/2 + j*oranges+k*bananas

                # Si el fill supera la capacidad, se termina el ciclo, pues las
                # sucesivas comprobaciones serían innecesarias.
                if fill > capacity or fill < max_filled:
                    break

                new_fill = fill

    # Establecimiento de max_filled.
    if(new_fill > max_filled and new_fill <= capacity):
        max_filled = new_fill

print "Max fill:", max_filled,
print "con y=(x*o+y*b)/2+(j*o+k*b)",
print "para o=" + str(oranges) + " b=" + str(bananas),
print "x="+str(x) + " y="+str(y) + " j="+str(j) + " k="+str(k)
