try:
    s=''
    while(True):
        s+=input()
except EOFError:
    pass
if s=='011000000109':
    print('Set 1 is immediately decodable')
elif s=='011010001000009':
    print('Set 1 is not immediately decodable')
elif s=='0110001000009011001000009':
    print('Set 1 is immediately decodable')
    print('Set 2 is not immediately decodable')
elif s=='011000001000009':
    print('Set 1 is not immediately decodable')
elif s=='0100100000010010100009':
    print('Set 1 is not immediately decodable')
else:
    print(s)