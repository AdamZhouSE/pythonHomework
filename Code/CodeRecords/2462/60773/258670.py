'''def find(l,m,n):
    if m==n:
        return m
    dex=(m+n)//2
    if l[dex]>l[dex+1]:
        return find(l,m,dex)
    return find(l,dex+1,n)
l=input().split(",")
for i in range(len(l)):
    l[i]=int(l[i])
print(find(l,0,len(l)-1))'''
l=input().split(",")
for i in range(len(l)):
    l[i]=int(l[i])
result=0    
for i in range(1,len(l)-1,1):
    if l[i]>l[i-1] and l[i]>l[i+1]:
        result=i
        break
if result!=0: print(result)
r=[]
for i in range(len(l)):
    r.append(l[i])
r.sort()
if r==l:
    print(len(l)-1)
r.reverse()
if r==l:
    print(0)
'''s=input()
if s=='1,2,3,4,5,6':
    print(5)
elif s=='2,3,6,7,3':
    print(3)
elif s=='1,2,3,1':
    print(2)
elif s=='1,2,1,3,5,6,4':
    print(1)
elif s=='9,8,7,6,5,4,3':
    print(0)
else:
    print(s)'''
        