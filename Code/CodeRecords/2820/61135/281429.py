n=int(input())
hour=0
minu=-1
num=1
minnum=1
for a in range(0,n):
    inpu=input().split(" ")
    listin=list(int(b) for b in inpu)
    if(listin[0]==hour and listin[1]==minu):
        num=num+1
    else:
        hour=listin[0]
        minu=listin[1]
        if(num>minnum):
            minnum=num
        num=1
print(minnum)