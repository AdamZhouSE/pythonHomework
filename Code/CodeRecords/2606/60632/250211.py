data = eval(input())
k = int(input())
if k in data:
    print(data.index(k))
else:
    print(-1)
