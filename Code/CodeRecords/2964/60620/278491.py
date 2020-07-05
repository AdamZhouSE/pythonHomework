n=int(input())
a=[]
for i in range(n):
    s=input()
    a.append(s)
def similar(s1,s2):
    if len(s1) < len(s2):
        return similar(s2,s1)
    if len(s2) == 0:
        return len(s1)
    previous= range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current= [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous[j + 1] + 1
            deletions = current[j] + 1
            substitutions = previous[j] + (c1 != c2)
            current.append(min(insertions, deletions, substitutions))
        previous= current
    return previous[-1]
n1=0
n2=0
n3=0
n4=0
n5=0
n6=0
n7=0
n8=0
for i in range(n):
    for j in range(i+1,n):
        if (similar(a[i],a[j])==1): n1+=1
        if (similar(a[i],a[j])==2): n2+=1
        if (similar(a[i], a[j]) == 3): n3 += 1
        if (similar(a[i], a[j]) == 4): n4 += 1
        if (similar(a[i], a[j]) == 5): n5 += 1
        if (similar(a[i], a[j]) == 6): n6 += 1
        if (similar(a[i], a[j]) == 7): n7 += 1
        if (similar(a[i], a[j]) == 8): n8 += 1
print(n1,n2,n3,n4,n5,n6,n7,n8,end=' ')