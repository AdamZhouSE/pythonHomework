n=int(input())
lists=[]
for i in range(pow(2,n)):
    a=list(bin(i))[2:]
    x=[]
    for j in range(n-len(a)):
        x.append("0")
    for j in a:
        x.append(j)
    lists.append(x)
elses=[]
for i in lists:
    location=0
    for j in range(len(i)):
        if i[j]=="0":
            location=j
            break
    if(j!=0):
        count=0
        for x in i[j:]:
            if x=="1":
                count+=1
        if(count==0):
            elses.append(i)
print(elses)






















