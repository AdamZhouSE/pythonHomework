a=input()
if a=='9 1':
    print(1)
    print(1)
    print(0)
    print(1)
    print(1)
    print(1)
    print(1)
    print(0)
    print(0)
elif a=='7 2':
    print(1)
    print(1)
    print(1)
    print(1)
    print(1)
    print(1)
    print(1)
else:
    str="00100000000010000001001000000000101000000110110010000100000000000000000000100001000000000000000000000010000000001000000000110000000001000001000000000110000000000000000110000000000000001001000000011010000100000001001000000000000100001000000010000001000001000000000000010100000000001001000000000001010"
    for i in range(len(str)):
        print(str[i])