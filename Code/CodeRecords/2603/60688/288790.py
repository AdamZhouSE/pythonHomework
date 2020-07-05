numslist=eval(input())
k=int(input())
num=set()
for i in range(0,len(numslist)):
    for j in range(i+1,len(numslist)):
        num.add(abs(numslist[i]-numslist[j]))
numsres=list()
for n in num:
    numsres.append(n)
numsres=sorted(numsres)
print(numsres[k-1])