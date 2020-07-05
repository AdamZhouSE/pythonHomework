def chazhao13(a,k):
    a.sort()
    return a[k-1] 
n=int(input())
a=[]
for i in range(0,n):
    l=input().split(',')
    l=[int(x) for x in l]
    for x in l:
        a.append(x)
k=int(input())
print(chazhao13(a,k))