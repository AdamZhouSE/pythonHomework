n=int(input())
a=[]
for i in range(n):
    s=input()
    a.append(s)
for i in range(len(a)): 
    tem=list(a[i])
    tem.sort()
    a[i]="".join(tem)
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]==a[j]:
            a.pop(j)
print(len(a))