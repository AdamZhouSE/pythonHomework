def QA(s:str):
    return s=='Q' or s=='A'

s=list(filter(QA,list(input())))
L=len(s)
ans=0
for i in range(L):
    if s[i]=="Q":
        for j in range(i+1,L):
            if s[j]=="A":
                for k in range(j+1,L):
                    if s[k]=="Q":
                        ans+=1
print(ans,end="")