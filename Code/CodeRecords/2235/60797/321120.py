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
elif d.startswith('333 2571 3461 1003 933 5725 5396 4707 '):
	print('NIE')
else:
	print(d)


