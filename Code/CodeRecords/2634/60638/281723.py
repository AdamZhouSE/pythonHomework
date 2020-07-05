numbers=list(map(int,input()[1:-1].split(",")))
k=int(input())
res=[]
for i in range(0,len(numbers)):
    for j in range(i+1,len(numbers)):
        res.append([numbers[i]/numbers[j],numbers[i],numbers[j]])
res.sort(key=lambda x:x[0])
result=[res[k-1][1],res[k-1][2]]
print(result)