info=input()[0:-2].split(' ')
a=[int(y) for y in info]
a.reverse()
b=[str(y) for y in a]
print(int(''.join(b)))


