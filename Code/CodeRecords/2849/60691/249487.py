s1 = input()
s2 = input()

if int(s1) == 1:
    print(s1)

l = s2.split(" ")
l.sort()

boolean = True

for i in range(1, len(l)):
    if int(l[i]) % int(l[0]) != 0:
        boolean = False
        break

if boolean:
    print(l[0])
else:
    print(-1)


