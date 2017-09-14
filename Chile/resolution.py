#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 03/09/17


# Verifica bloques subsiguientes de un string, para verificar si más índices
# forman parte del substring más largo.
def verify_more(s, i, block_size):
    while(i+block_size < len(s)):

        str = s[i:i+block_size]
        if s.count(str) > 1:
            block_size += 1
        else:
            # Se decrementa block size al no haber coincidencia
            return block_size-1

    return block_size


f = open("level15.txt")
s = f.read()
f.close()

block_size = 10

max_len = 0
max_str = ""

while(block_size < len(s)):
    print "Block size:", block_size

    for i in range(0, len(s)-1-block_size):
        str1 = s[i:i+block_size]
        if(s.count(str1) > 1):
            if(len(str1) > max_len):

                # Verificación de si en bloques subsiguientes también hay
                # coincidencia
                new_block_size = verify_more(s, i, block_size)
                max_str = s[i:i+new_block_size]
                max_len = len(max_str)

                print "Str:", max_str, "- Len:", max_len
                print ""

                if(new_block_size > block_size):
                    block_size = new_block_size
                    break
    block_size += 1

print "Finish!"
