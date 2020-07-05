string=eval(input())
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
def swap(temp,i,j):
    t = temp[i]
    temp[i] = temp[j]
    temp[j] = t
def swapEqual(str1,str2):
    temp=list(str1)
    for i in range(len(temp)):
        for j in range(i+1,len(temp)):
            swap(temp,i,j)
            if(''.join(temp)==str2):
                return True
            swap(temp,i,j)
    return False
for i in string:
    set.append([i])
for i in range(len(string)):
    for j in range(i+1,len(string)):
        if(swapEqual(string[i],string[j])):
            union(string[i],string[j])
print(len(set))

