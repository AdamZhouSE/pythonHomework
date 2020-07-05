input=input()
a=input.replace('[','')
b=a.replace(']','')
c=b.replace('\n','')
d=c.split(',')
result=list()
for x in range(0,len(d)):
    num=0
    for y in range(x+1,len(d)):
        if d[y]<d[x]:
            num=num+1
    result.append(num)
print(result)