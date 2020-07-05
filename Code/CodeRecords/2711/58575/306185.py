res=[]

words=input()[1:-1].split(",")
i=0
while i<len(words):
    words[i]=words[i][1:-1]
    i+=1

i=0
while i<len(words)-1:
    j=i+1
    while j<len(words):
        k=0
        while words[i][k]==words[j][k]:
            k+=1
        w=k+1
        while words[i][w]==words[j][w]:
            w+=1
        if words[i]==words[j][0:k]+words[j][w]+words[j][k+1:w]+words[j][k]+words[j][w+1:]:
            judge=False
            for resIndex in res:
                if words[i] in resIndex:
                    resIndex.append(words[j])
                    judge=True
                elif words[j] in resIndex:
                    resIndex.append(words[i])
                    judge=True
            if judge==False:
                res.append([words[i],words[j]])
        j+=1
    i+=1

sum=0
for i in res:
    sum+=len(i)
print(len(res)+len(words)-sum)