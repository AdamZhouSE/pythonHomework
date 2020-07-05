n,m=map(int,input().split(' '))
gold=list(map(int,input().split(' ')))
relations=[]
def union(i,j):
    global friends
    record_i=-1
    record_j=-1
    for k in range(len(friends)):
        if(i in friends[k]):
            record_i=k
        if(j in friends[k]):
            record_j=k
        if(record_i!=-1 and record_j!=-1):
            break
    if(record_j!=record_i):
        for a in friends[record_i]:
            if a not in friends[record_j]:
                friends[record_j].append(a)
    del friends[record_i]
friends=[[i+1] for i in range(n)]
for i in range(m):
    relations.append(list(map(int,input().split(' '))))
for i in relations:
    union(i[0],i[1])
sum=0
for i in friends:
    record=float('Inf')
    for j in i:
        if(gold[j-1]<record):
            record=gold[j-1]
    sum+=record
print(sum)
