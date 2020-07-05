source=eval(input())
counts=[]
for i in range(len(source)):
    count=0
    for j in range(i+1,len(source)):
        if(source[j]<source[i]):
            count+=1
    counts.append(count)
print(counts)