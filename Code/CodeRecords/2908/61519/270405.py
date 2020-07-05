n=int(input())
a=[]
b=[]
for i in range(n):
    s=input().strip()
    a.append(s)
for i in range(len(a)): 
    tem=list(a[i])
    tem.sort()
    a[i]="".join(tem)
b.append(a[0])
for i in range(1,len(a)-1):
    if a[i] not in b:
        b.append(a[i])
print(len(b))