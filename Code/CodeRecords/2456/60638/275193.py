numbers=list(map(int,input()[1:-1].split(",")))
res=[]
for i in range(0,len(numbers)):
    count=0
    for j in range(i,len(numbers)):
        if numbers[j]<numbers[i]:
            count=count+1
    res.append(count)
print(res)