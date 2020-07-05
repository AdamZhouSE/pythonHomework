n=int(input())
list1=list(map(int,input().split(",")))
len1=0
sum2=0
for i in range(1,len(list1)+1):
    sum1=0
    for j in range(0,len(list1)-i+1):
        sum=0
        for k in range(0,i):
            sum=sum+list1[j+k]
        if sum>=n:
            sum1=sum
            break
    if sum1>=n:
        len1=i
        sum2=sum1
        break
if sum2>=n:
    print(len1)
else:
    print(0)
