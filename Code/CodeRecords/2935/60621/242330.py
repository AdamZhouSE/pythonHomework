a=input()
count=0
t1,t2=[],[]
for i in range(len(a)):
    if(a[i]=="Q"):
        count+=1

    t1.append(count)

t2=[count-x for x in t1]
ans=0
for i in range(len(a)):
    if(a[i]=="A"):
        ans+=(t1[i]*t2[i])
print(ans,end="")