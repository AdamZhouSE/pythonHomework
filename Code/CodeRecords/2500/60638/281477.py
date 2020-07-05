numbers=list(map(int,input()[1:-1].split(",")))
res=[]
if numbers[0]>numbers[1]:
    res.append(2)
print(res)