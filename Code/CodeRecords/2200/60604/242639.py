a=input()
#print(a)
b=input()
#print(b)
m=int(input())
res=[]
for i in range(1,len(a)):
    for j in range(len(a)-i+1):
        count=0
        tmp=b[j:j+i]
        #print(tmp)
        for k in tmp:
            if k=='0':
                #print(k)
                count+=1
        if m>=count and not tmp in res:
            res.append(tmp)
count=0
for i in b:
    if i=='0':
        count+=1
if m>=count:
    res.append(b)
print(len(res))