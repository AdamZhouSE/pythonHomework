
time=int(input())
result=[]

while time>0:
    sum=0
    num=int(input())
    for i in range(1,num+1):
        sum=sum+i**2

    time=time-1
    result.append(sum)
for res in result:
    print(res)

