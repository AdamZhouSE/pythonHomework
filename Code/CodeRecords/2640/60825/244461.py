S=input()
T=input()
res=""
lenRes=99999

for i in range(len(S)):
    for j in range(i+1, len(S)):
        flag=0
        for c1 in T:
            if c1 not in S[i:j+1]:
                flag=1
                break
        if(flag==0 and len(S[i:j+1])<lenRes):
            lenRes=len(S[i:j+1])
            S=S[i:j+1])

print(res)