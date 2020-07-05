arr=list(range(101))
arr=list(map(str,arr))
arr.sort()
arr.pop(0)
for n in arr:
    print(n)