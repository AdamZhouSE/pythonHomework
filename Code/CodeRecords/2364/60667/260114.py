n = int(input())
c = 0
for i in range(n+1):
    for j in range(10):
        if str(i).count(str(j)) >= 2:
            c += 1
            break
print(c)            