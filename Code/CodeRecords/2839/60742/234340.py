n = int(input())
l = []
for i in range(n):
    name = input()
    if name in l:
        print ("YES")
    else:
        print ("NO")
        l.append(name)