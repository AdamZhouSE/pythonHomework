data=input()
datastr=data.split(',')
data=list(map(int,datastr))
len1=len(data)
nstr=input()
lenth=len(nstr)-1
n=int(nstr)
i=1
count=0
while i<=lenth:
    count+=len1**i
    i+=1

i=0

while (i<lenth+1 and lenth>=0):
    if(data[i]<int(n/(10**lenth))):
        count+=len1**lenth
        i+=1
        continue
    if(data[i]==int(n/(10**lenth))):
        lenth-=1
        i=0
        n=n%(10**lenth)
        continue
    if(data[i]>int(n/(10**lenth))):
        break
print(count)