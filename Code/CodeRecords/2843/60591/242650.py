n = eval(input())
a = list(map(int,input().split(" ")))
a.reverse()
b = []
b.append(a[0])
for x in range(len(a) - 1):
    b.append(a[x] + a[x+1])
b.reverse()
b = list(map(str,b))
print(" ".join(b))

