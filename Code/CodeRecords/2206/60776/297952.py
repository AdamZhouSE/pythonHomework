a=int(input())
for k in range(0,a):
    a=int(input())
    result=0
    index=1
    for i in range(1,a+1):
        temp=1
        for j in range(index,index+i):
            temp=temp*j
        index=index+i
        result=result+temp
    print(result)