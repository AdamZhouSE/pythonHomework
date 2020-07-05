T=int(input())
while T>0:
    n=int(input())
    num = [int(n) for n in input().split()]
    num=sorted(num)
    index=0
    while index<=len(num):
        if index+1<len(num):
            i=num[index]
            num[index]=num[index+1]
            num[index+1]=i
        index+=2
    count=0
    for i in num:
        count+=1
        if count==len(num):
            print(i)
        else:
            print(i,end=' ')
    T-=1