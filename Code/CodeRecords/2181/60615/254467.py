count=int(input())
result=[]
while count>0:
    index=int(input())
    result.append(index*(index*index+1))
    count=count-1
for i in result:
    print(i)