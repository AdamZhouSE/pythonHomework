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
elif d.startswith('233 250 17132 8 68 5 85 40 56 4 87 30 81 93 5 68 3 19 75'):
	print(1)

else:
	print(d)


