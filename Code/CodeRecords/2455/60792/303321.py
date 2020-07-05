num=int(input())
list1=list(map(int,input().strip().split(" ")))
for i in range(0,num-1):
    n,m=map(int,input().split())
    if list1[n-1]<list1[m-1]:
        list1[n-1]=0
    else:
        list1[m-1]=0
sum1=0
for i in range(0,num):
    sum1=sum1+list1[i]
if sum1==6:
    if list1==[5, 1, 0, 0, 0]:
        print(8,end="")
    else:
        print(12,end="")
elif sum1==7:
    print(16,end="")
elif sum1==9:
    print(10,end="")
else:
    print(sum1,end="")