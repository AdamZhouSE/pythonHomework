a = eval(input())
k = int(input())
a.sort(key=lambda x:x[0]**2+x[1]**2)
res = a[:k]
print(res)