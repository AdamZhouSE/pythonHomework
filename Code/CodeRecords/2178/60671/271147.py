length=int(input())
str0=input()
list0=str0.split()
listnum=[]
for c in list0:
    listnum.append(int(c))
allsub=[]
strr=""
for i in range(length):
    strr+=str(listnum[i])
    for j in range(i+1):
        temp=strr[j:]
        same=False
        for s in allsub:
            if(s==temp):
                same=True
                break
        if(not same):
            allsub.append(temp)
    print(len(allsub))
    