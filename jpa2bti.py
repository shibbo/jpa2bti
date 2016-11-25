# jpa to btu but colorless

import binascii, os, struct, sys

def convertTEX(offset, data, length, datasize):
    offset+=0x20
    bytelist = []
    name = sys.argv[1].replace("jpa", "bti")

    thing = open(name, 'wb')

    while offset < datasize:
        shit, = struct.unpack_from('>B', data, offset)
        bytelist.append(shit)
        offset+=1

    bytearr = bytearray(bytelist) # put all bytes into array

    thing.write(bytearr) # write the array to file :D

if len(sys.argv) == 1:
    print('usage: jpa2bti.py infile.jpa')
    sys.exit()
else:
    with open(sys.argv[1], 'rb') as f:
        data = f.read()

i = 0
while i < len(data):
    jpa = struct.unpack_from('>4sI', data, i)
    header, size = jpa

    if header == b'TEX1':
        convertTEX(i, data, size, len(data))
        i+=size # this should instantly jump to EOF
    else:
        i+=8
