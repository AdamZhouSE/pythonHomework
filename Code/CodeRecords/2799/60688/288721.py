times=int(input())
numslist=input().split(" ")
numslist=list(int(a) for a in numslist)
res="Yes"
for i in range(0,times):
    while(numslist[i]%3==0):
        numslist[i]=numslist[i]/3
    while (numslist[i] % 2 == 0):
        numslist[i] = numslist[i] / 2
    if(i!=0):
        if(numslist[i]!=numslist[i-1]):
            res="No"
            break
print(res)