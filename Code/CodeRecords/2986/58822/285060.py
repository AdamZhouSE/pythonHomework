target=input()
n=input()
if(target==n):
    print(0)
    exit()
times=0
ret=[]
ren=[]
l=""
times=0
same=0
dif=0
for i in range(0,len(target)):
    k=0
    for j in range(same,len(n)):
        if(j==same and k==1):
            break
        if(target[i]==n[j]):
            same+=j
            j+=1
            #same+=j
            k=1
        if (k == 1):
            break
    if(k==1):
        dif+=1


print(dif+1)