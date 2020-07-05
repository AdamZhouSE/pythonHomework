string=list(input())
pairs=eval(input())
set=[]
def search(i,set):
    for j in range(len(set)):
        if(i in set[j]):
            return j
    return -1

def union(a,b):
    global set
    i,j=search(a,set),search(b,set)
    if(i!=j):
        for k in set[i]:
            if(k not in set[j]):
                set[j].append(k)
    set[j].sort()
    del set[i]
for i in range(len(string)):
    set.append([i])
for i in pairs:
    union(i[1],i[0])
for i in set:
    temp = []
    for j in i:
        temp+=string[j]
    temp.sort()
    for j in range(len(i)):
        string[i[j]]=temp[j]
print("".join(string))