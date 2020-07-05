stones=input().split(",")
stones=list(int(a) for a in stones)
stones=sorted(stones)
i=0
mi=len(stones)
ma=max(stones[-1]-stones[1],stones[-2]-stones[0])-len(stones)+2
for j in range(len(stones)):
    while(stones[j]-stones[i]>=len(stones)):
        i=i+1
    if(j-i+1==len(stones)-1 and stones[j]-stones[i]==len(stones)-2):
        mi=min(2, mi)
    else:
        mi=min(mi,len(stones)-j+i-1)
print("[",end="")
print(mi,end=", ")
print(ma,end="]\n")