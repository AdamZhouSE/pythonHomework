t = input()
z = input()
z = list(map(int, z.split(' ')))
z = z[2]

s = input()
s = list(map(int, s.split(' ')))
k = input()
k = list(map(int, k.split(' ')))
for i in s:
    k.append(i)
k.sort()
print(k[z-1])

