import binascii

str = [b'class', b'function', b'method']

for i in str:
    print(type(i), binascii.hexlify(i), len(i))