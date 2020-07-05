a=input()
a=int(a)
b=input().split()
c=input().split()
d,e={},{}
for i in range(a):
    d[b[i]]=i
    e[c[i]]=i
count=0
for i in d.keys():
    for j in e.keys():
        if(d[i]<d[j] and e[i]>e[j])or(d[i]>d[j] and e[i]<e[j]):
            count+=1
print(count//2)