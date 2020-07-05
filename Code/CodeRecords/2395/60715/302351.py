def sort1(num):
    ls=[]
    count=0
    for i in num:
        if i==0:
            count+=1
        else:
            ls.append(i)
    while count>0:
        ls.append(0)
        count-=1
    return ls
T=int(input())
while T>0:
    n=int(input())
    num = [int(n) for n in input().split()]
    for i in range(len(num)-1):
        if num[i]==0:
            num=sort1(num)
        if num[i]==num[i+1]:
            num[i]*=2
            num[i+1]=0
    count=0
    for i in num:
        count+=1
        if count==len(num):
            print(i)
        else:
            print(i,end=' ')
    T-=1