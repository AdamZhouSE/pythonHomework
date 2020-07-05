n = int(input())
a = input().split(" ")
a = [int(x) for x in a]
# 下面删除数组中有倍数关系的：
i = 0
while i < len(a) - 1:
    j = i + 1
    while j<len(a):
        if a[j] % a[i] == 0:
            del a[j]
            j=j-1
        elif a[i]%a[j]==0:
            del a[i]
            i=i-1
            break
        j=j+1
    i = i + 1
n = len(a)
m = min(a)
for i in range(1,m):
    if i*i>m:
        break
maxTotal=i+1#最大可能的公因数数
if n==1 :
    if a[0]==1:
        print(1)
    else:
        result=0
        for i in range(1,int(a[0]/2)+1):
            if a[0]%i==0:
                result=result+1
            if result>maxTotal:
                break
        print(result+1)

else:
    result = 0
    for i in range(1, int(m/2)+1):
        j = 0
        while j < n:
            if a[j] % i != 0:
                break
            j = j + 1
        if j == n:
            result = result + 1
        if result>=maxTotal:
            break

    print(result)
