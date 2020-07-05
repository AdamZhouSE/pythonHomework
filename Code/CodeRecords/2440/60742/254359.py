a = eval(input())
a = [int(i) for i in a]
n = len(a)
for i in range(1,n):
    for j in range(i):
        if a[i]<a[j]:
            a.insert(j,a.pop(i))
            break
print(a)