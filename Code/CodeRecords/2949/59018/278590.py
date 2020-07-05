inp=input()
info=inp[0:-2].split(' ')
a=[int(y) for y in info]
a.reverse()
b=[str(y) for y in a]
print(inp)
print(int(''.join(b)))


