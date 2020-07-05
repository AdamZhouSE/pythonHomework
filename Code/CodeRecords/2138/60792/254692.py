list1=list(map(int,input().split(",")))
n=int(input())
flag=False
len=len(list1)
for i in range(0,len):
    sum=0
    for j in range(0,len-i):
        sum=sum+list1[i+j]
        if sum%n==0:
            flag=True
            break
    if flag:
        break
print(flag)
        