l=eval(input())
res=[]
for i in range(len(l)):
    sum=0
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            sum+=1
    res.append(sum)
print(res)