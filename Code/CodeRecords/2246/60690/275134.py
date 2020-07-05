n=input()
list=[]
for e in n:list.append(e)
length=len(n)
low,high=0,0

while len(str(2**low))<length: low+=1
high=low
while len(str(2**high))==length: high+=1
res=False
for i in range(low,high):
    Bn=str(2**i)
    l=list[:]
    for j in range(len(Bn)):
        if Bn[j] in l:l.remove(Bn[j])
    if len(l)==0:
        res=True
        break
print(res)