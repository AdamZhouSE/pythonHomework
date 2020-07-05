n=list(input())
dA=0
dB=0
stage=0
ans=[0 for i in range(len(n))]
for i in range(len(n)):
    if stage==0:#add a letter to A
        ans[i]=0
        if n[i]=="(":
            dA+=1
            stage=1
        else:
            dA-=1
    elif stage==1:
        if n[i]=="(":
            ans[i]=1
            dB+=1
            stage=2
        else:
            ans[i]=0
            dA-=1
            stage=0
    elif stage==2:
        if n[i]=="(":
            ans[i]=1
            if dB==dA:
                for j in range(i):
                    if ans[j]==1:
                        ans[j]=0
                        break
                dA+=1
            else:
                dB+=1
        else:
            ans[i]=1
            dB-=1
            if dB==0:
                stage=1
print(ans)