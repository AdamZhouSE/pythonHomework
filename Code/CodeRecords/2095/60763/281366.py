a = input()
b = input()
c = ''+bin(int(a,2) + int(b,2))
print(c[c.find('b')+1:len(c)])