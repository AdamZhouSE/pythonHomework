numbers=list(map(int,input()[1:-1].split(",")))
k=int(input())
x=int(input())
res=[]
i=0
numbers.sort()
while len(res)<k:
    for j in range(0,len(numbers)):
        if abs(x-numbers[j])==i:
            res.append(numbers[j])
    i=i+1
result=res[0:k]
result.sort()
print(result)