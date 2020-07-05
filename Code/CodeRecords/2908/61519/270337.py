n=int(input())
a=[]
b=[]
for i in range(n):
    s=input()
    a.append(s)
for i in range(len(a)): 
    tem=list(a[i])
    tem.sort()
    a[i]="".join(tem)
b.append(a[0])
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
print(b)
print(len(b))