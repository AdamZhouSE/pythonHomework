t=int(input())
for i in range(0,t):
    n=int(input())
    list1=input().split()
    list1=list(map(int,list1))
    num=[0]*n
    for j in list1:
        num[j-1]=num[j-1]+1
    if(0 in num):
        a=num.index(0)
    else:
        a=-1
    if(2 in num):
        b=num.index(2)
    else:
        b=-1
    print(b+1,a+1)
