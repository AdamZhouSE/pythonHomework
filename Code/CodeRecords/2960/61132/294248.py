def findsubstr2(s,le,li):
    tmp=[]
    index=0
    while index+le<=len(li):
        tmp.append(''.join(li[index:index+le]))
        index+=1
    return tmp

def equal(l1,l2):
    for i,j in zip(l1,l2):
        if i!=j and i!='*' and j!='*':
            return False
    return True

m,n=input().split()
a=list(input().split()[0])
b=list(input().split()[0])
sum=0
start=[]
index=1
for j in findsubstr2('',len(a), b):
    if equal(a, j):
        sum += 1
        start.append(str(index))
    index+=1

print(sum,end='')
print()
start.sort()
print(' '.join(start)+' ')