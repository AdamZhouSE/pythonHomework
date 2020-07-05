n=int(input())
l1=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
for i in l2:
    index=0
    Sum=l1[0]
    while i>Sum:
        index+=1
        Sum+=l1[index]
    print(index+1)
