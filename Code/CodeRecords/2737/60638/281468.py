numbers=list(map(int,input()[1:-1].split(",")))
numbers.sort()
res=[]
for i in range(0,len(numbers)):
    count=1
    k=numbers[i]
    while i<len(numbers)-1 and numbers[i]==numbers[i+1]:
        count=count+1
        i=i+1
    if count>len(numbers)//3:
        res.append(k)
print(res)