num=eval(input())
counts=[]
for i in range(0,len(num)):
    temp=0
    for j in range(i+1,len(num)):
        if num[j]<num[i]:
            temp+=1
    counts.append(temp)
print(counts)