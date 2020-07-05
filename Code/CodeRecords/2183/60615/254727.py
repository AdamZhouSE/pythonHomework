count=int(input())
result=[]
while count>0:  #count sub
    sum=0
    n=int(input())
    start=1
    for i in range(1,n):
        start=start+2*i
    for i in range(start,start+2*n):
        sum=sum+i
    result.append(sum)
    count=count-1
for i in result:
    print(i)
