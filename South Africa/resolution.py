#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 02/09/17

def challenge_hash(s):
    h = 7
    letters = "acdegilmnoprstuw"

    for i in range(0, len(s)):
        h = (h * 37 + letters.index(s[i]))

    return h

# Reverse de hash
def challenge_hash_reverse(h):
    s = ""
    letters = "acdegilmnoprstuw"

    while(h/37 > 0):
        # Resto de suma palabra.
        x = h%37

        # Reducción de h a la próxima palabra (sin tener en cuenta resto).
        h = h/37

        s += letters[x]

    return s[::-1]

#v = challenge_hash("mercadoli")
#print v
print challenge_hash_reverse(24785204182557)
