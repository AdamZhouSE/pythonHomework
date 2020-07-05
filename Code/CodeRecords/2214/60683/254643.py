a = input().split('+')
b = input().split('+')
realA = int(a[0])
realB = int(b[0])
Ai = int(a[1][:-1])
Bi = int(b[1][:-1])
resR = realA * realB - Ai * Bi
resi = realA * Bi + realB * Ai
print(str(resR)+'+'+str(resi)+'i')
