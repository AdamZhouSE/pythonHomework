def count(num,n):
    count=0
    for i in num:
        if i==n:
            count+=1
    return count
T=int(input())
while T>0:
    N=int(input())
    num = [int(n) for n in input().split()]
    c=[]
    for i in num:
        if i not in c:
            c.append(i)
    for i in c:
        if count(num,i)%2!=0:
            print(i)
    T-=1