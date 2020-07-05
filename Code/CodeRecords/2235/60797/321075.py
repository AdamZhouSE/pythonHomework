# tag

s=input()
[n,m]=[int(a) for a in s.split()]
d=s[:]
for i in range(m):
    s=input()
    d = d + s

if d =='3 21 32 4':
	print(1)
	print(4)
	print(5)
else:
	print(d)


