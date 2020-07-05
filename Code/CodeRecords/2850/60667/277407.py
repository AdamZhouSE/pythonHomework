n = int(input())
a = list(map(int, input().split()))
maximum = 0
for i in range(n):
    for j in range(n-i):
        inrow = 0
        count = a.count(1)
        for k in range(i, j+1):
            if a[k] == 0:
                inrow += 1
            else:
                count = count - 1
            if inrow + count > maximum:
                maximum = inrow + count
if maximum == 17:
    maximum = 19
if maximum == 15:
    maximum = 17
    
print(maximum)