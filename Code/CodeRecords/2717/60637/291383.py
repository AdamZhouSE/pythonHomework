equations=eval(input())
letters=[]
for i in equations:
    for j in [0,3]:
        if(i[j] not in letters):
            letters.append(i[j])
set=[]
def union(a,b):
    global set
    i,j=map(int,search(a,b))
    if(i!=j):
        for k in set[i]:
            if(k not in set[j]):
                set[j].append(k)
        del set[i]
def search(a,b):
    global set
    record_a=-1
    record_b=-1
    for i in range(len(set)):
        if(a in set[i]):
            record_a=i
        if(b in set[i]):
            record_b=i
    return [record_a,record_b]
for i in letters:
    set.append([i])
for i in equations:
    if(i[1]=='='):
        union(i[0],i[3])
result='true'
for i in equations:
    if(i[1]=='!' ):
        i,j=map(int,search(i[0],i[3]))
        if(i==j):
            result='false'
print(result)
