aa = input()
a = input().split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
list.sort(a)
ans = 0
for i in range(1, a[0]+1):
    t = 0  
    for k in range(len(a)):
        if a[k] % i != 0:
            t = 1
    if t == 0:
        ans = ans + 1
print(ans)