s=input()[1:-1].split(",")
for i in range(len(s)): s[i]=int(s[i])
s.sort()
little=[]
big=[]
res=[]
li,bi=0,0
for i in range(int((len(s)+1)/2)):
    little.append(s[i])
for i in range(int((len(s)+1)/2),len(s)):
    big.append(s[i])
for i in range(len(s)):
    if i%2==0:
        res.append(little[li])
        li+=1
    else:
        res.append(big[bi])
        bi+=1
print(res)