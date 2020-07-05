n=input()
b=list(eval(n))
b.sort()
li=[]
c=int(len(b)/2)
le=1
if(len(b)==2 and b[0]==b[1]):
    print(b[0])
    exit()
for i in range(1,len(b)):
    current=b[i]
    if(i==0):
        continue
    if(b[i]==b[i-1]):
        le+=1
        if(le>c):
            li.append(b[i])
    else:
        le=1
k=set(li)
for i in range(len(k)):
    print(k.pop())