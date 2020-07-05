k=int(input())
dic={}
names=[]
scores=[]
for i in range(k):
    nm=input().split(' ')
    n=nm[0]
    m=int(nm[1])
    names.append(n)
    scores.append(m)
    if n in dic:
        dic[n]+=m
    else:
        dic[n]=m
highest=max(dic.values())
dic={}
for i in range(k):
    n=names[i]
    m=scores[i]
    if n in dic:
        dic[n]+=m
    else:
        dic[n]=m
    if dic[n]>=highest:
        print(n)
        break