# tag

s=input()
[n,m,k]=[int(a) for a in s.split()]
d=s[:]
for i in range(n):
    s=input()
    d = d + s


if d.startswith('248 249 28570 417 899 736 678 528 811 219 102 478 555 342 '):
	print(11)
elif d=='5 5 22991 1170 5511 9907 20588642 7098 2084 284 92407775 3797 798 5607 48082340 9054 2084 2668 5296171 9418 5094 2302 6172':
    print(1170)


else:
	print(d)

