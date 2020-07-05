count=int(input())
result=[]
while count>0:  #count sub
    sum=0
    n=int(input())
    for i in range(1,n+1):
        sum=sum+i
    sum=sum*4-n
    result.append(sum)
    count=count-1
for i in result:
    print(i)
