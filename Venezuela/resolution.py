#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Busca el primer índice no pintado teniendo en cuenta los elementos aún no
# pintados.
def get_first_index_not_stroked(lst, stroked, m):
    for x in lst:
        if x not in stroked:
            if(x >= m):
                return lst.index(x)

# Lista de prueba
#lst = [1, 4, 2, 1, 2, 1, 5, 4, 4, 4, 2]

#lst = [1, 3, 3, 1, 2, 1, 1, 1, 3, 1, 2]
lst = [1, 4, 5, 6, 7, 8, 15, 12, 9, 4, 9, 8, 12, 14, 22, 45, 67, 89, 87, 86, 85, 23, 56, 67, 21, 88, 11, 44, 56, 91, 67, 45, 45, 45, 45, 45, 44, 21, 89, 90, 90, 87, 45, 91, 12, 45, 57]

lst2 = lst
stroked = []


total_strokes = 0

# Recorrida de 1 al máximo de lista (puede haber pisos faltantes en la lista).
for m in range(1, max(lst)+1):
    #m = min([item for item in lst if item not in stroked])

    #first_index = lst.index()
    first_index = get_first_index_not_stroked(lst, stroked, m)

    # Conteo de Strokes indivuales
    indiv_strokes = 0

    # Flag que indica finalización de stroke.
    stroke_finished = False
    lst2 = lst[first_index:]

    #print "m", m
    if(m not in stroked):
        for x in lst2:
            # SI x es menor al mínimo.
            if(x<m):
                # Significa que el stroke ha finalizado.
                if not stroke_finished:
                    # Se suma uno.
                    indiv_strokes += 1
                # Se establece bandera de stroke finalizado en true.
                stroke_finished = True
            else:
                # Comienza nuevo Stroke.
                stroke_finished = False

        if not stroke_finished:
            indiv_strokes += 1

        stroked.append(m)

        #print "Actual", m
        #print "Strokes", indiv_strokes
        #print ""

        # Suma de strokes individuales al total.
        total_strokes += indiv_strokes

print total_strokes
