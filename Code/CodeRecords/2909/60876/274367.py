s=list(input())
maxl=int(input())
minsize=int(input())
maxsize=int(input())
temp=[]
length=len(s)
for i in range(0,length):
    for l in range(minsize,maxsize+1):
        if i+l>length:
            break
        li=[]
        for k in range(i,i+l):
            if s[k] not in li:
                li.append(s[k])
        if len(li)<=maxl:
            temp.append("".join(s[i:i+l]))
if temp==[]:
    print(0)
else:
    sum = []
    ci = []
    for item in temp:
        if item not in ci:
            ci.append(item)
            sum.append(1)
        else:
            index = ci.index(item)
            sum[index] += 1
    max = sum[0]
    l = len(sum)
    ind = 0
    for i in range(0, l):
        if sum[i] > max:
            max = sum[i]
            ind = i
    print(max)