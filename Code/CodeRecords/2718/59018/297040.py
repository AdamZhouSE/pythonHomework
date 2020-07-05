s=list(input())
exchange=eval(input())
i,j=0,0
while i<len(exchange):
    j=i+1
    while j<len(exchange):
        if exchange[j][0] in exchange[i]:
            exchange[i].append(exchange[j][1])
            exchange.pop(j)
            j=i+1
        elif exchange[j][1] in exchange[i]:
            exchange[i].append(exchange[j][0])
            exchange.pop(j)
            j=i+1
        else:
            j+=1
    i+=1
for x in exchange:
    x.sort()
    numlist=[]
    for k in x:
        numlist.append(s[k])
    numlist.sort()
    for k in range(len(x)):
        s[x[k]]=numlist[k]
print(''.join(s))