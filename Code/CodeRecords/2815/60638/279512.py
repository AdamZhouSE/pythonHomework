num=int(input())
numbers=list(map(int,input().split(" ")))
sum=0
count=0
for i in range(0,num):
    if(numbers[i]<=-1):
        sum=sum+abs(numbers[i]+1)
        count=count+1
    else:
        sum=sum+abs(1-numbers[i])
if count%2==1:
    if not numbers.__contains__(0):
        sum=sum+2
print(sum)