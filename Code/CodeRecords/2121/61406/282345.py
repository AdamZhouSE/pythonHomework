def Amn(m,n):
    result = 1
    if m==0:
        return 0
    else:
        for i in range(n-m+1,n+1):
            result = result*i
        return result


n = int(input())
count = 0
for i in range(1,n+1):
    count = count+Amn(i,10)-Amn(i-1,9)
print(count)