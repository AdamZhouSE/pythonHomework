l=eval(input())
res=[]
for i in range(len(l)):
    sum=0
    for j in range(i+1,len(l)):
        if i<j:
            sum+=1
    res.append(sum)
print(res)