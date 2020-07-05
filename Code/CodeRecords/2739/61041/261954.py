strin = input()
k = int(strin[0])
n = int(strin[3:len(strin)])
total = []
a = [0]*10
result = []
def func(n,r,m):
    if n<r:
        return
    if r==0:
        temp = []
        for i in range(0,m):
            temp.append(a[i])
        total.append(sorted(temp))
    else:
        a[m] = n
        func(n-1,r-1,m+1)
        func(n-1,r,m)
func(9,k,0)
total = sorted(total)
for i in range(0,len(total)):
    sum = 0
    for j in range(0,len(total[i])):
        sum+=total[i][j]
    if sum==n:
        result.append(total[i])
print(result)