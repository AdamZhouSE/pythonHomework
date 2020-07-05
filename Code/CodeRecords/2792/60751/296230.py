num=int(input())
sq=list(map(int,input().split(" ")))
count=0
shu=1
k=[]
for i in range(1,len(sq)):
    if sq[i]==1:
        count+=1
        k.append(shu)
        shu=1
    else:
        shu+=1
k.append(shu)
count+=1
print(count)
print(k[0],end="")
for i in range(1,len(k)):
    print(" "+str(k[i]),end="")
print()
