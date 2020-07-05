abc=input()
a=len(abc)
arr=list(map(int,abc[1:a-1].split(',')))
count = {}
ans = nonzero = 0
for x, y in zip(arr, sorted(arr)):

    if(x not in count):
        count[x]=1
    else:
        count[x] += 1
    if count[x] == 0:
        nonzero -= 1
    if count[x] == 1:
        nonzero += 1

    if (y not in count):
        count[y] = 1
    else:
        count[y] -= 1
    if count[y] == -1:
        nonzero += 1
    if count[y] == 0:
        nonzero -= 1

    if nonzero == 0:
        ans += 1
print(ans)
