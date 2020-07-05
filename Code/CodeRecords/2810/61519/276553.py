n=list(input())
res=[]
string=""
for i in range(len(n)):
    n[i]=int(n[i])
num=max(n)
for i in range(max(n)):
    for j in range(len(n)):
        if n[j]>0:
            string=string+"1"
            n[j]=n[j]-1
        else:
            string=string+"0"
    res.append(string)
    string=""
for i in range(len(res)):
    res[i]=int(res[i])
for i in range(len(res)):
    res[i]=str(res[i])
ans=" ".join(res)
print(num)
print(ans)