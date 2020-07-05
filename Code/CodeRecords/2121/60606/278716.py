def accumulate(n):
    if n == 1:
        return 10
    else:
        temp=9
        for i in range(n-1):
            temp*=(9-i)
        return temp
exp = int(input())
sum = 0
for i in range(1,exp+1):
    sum += accumulate(i)
print(sum)
