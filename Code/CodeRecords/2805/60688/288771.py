times=int(input())
numslist=input().split(" ")
numslist=list(int(a) for a in numslist)
maxlen=1
len=1
for i in range(1,times):
    if(numslist[i]>numslist[i-1]):
        len=len+1
    else:
        if(len>maxlen):
            maxlen=len
        len=1
if(len>maxlen):
    maxlen=len
print(maxlen)