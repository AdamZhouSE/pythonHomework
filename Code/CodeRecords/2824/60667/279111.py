s = list(input().split())
n = int(s[0])
t = int(s[1])
c = int(s[2])
count = 0
criminals = list(map(int, input().split()))
for i in range(n-c+1):
    check = True
    for j in criminals[i:i+c]:
        if j > t:
            check = False
            break
    if check:
        count += 1
print(count)        