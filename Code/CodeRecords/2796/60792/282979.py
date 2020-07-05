def issquare(n):
    num=0
    for i in range(1,n+1):
        if i*i>=n:
            num=i
            break
    if num*num==n:
        return True
    else:
        return False

n=int(input())
list1=list(map(int,input().split(" ")))
list1.sort()
maxnum=-1
for i in range(0,n):
    if not issquare(list1[i]):
        maxnum=list1[i]
print(maxnum)   