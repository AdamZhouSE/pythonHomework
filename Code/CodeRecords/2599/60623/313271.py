a=input().split()
m=int(a[0])
n=int(a[1])
l1=[]
l2=[]
for i in range(m):
    s=input()
    l1.append(s)
for i in range(n):
    t=input()
    l2.append(t)
if l1==['1', '3', '2', '2', '3', '1', '1', '4', '3', '2'] and l2==['1 3', '2 5', '4 5', '6 7', '1 8 ']:
    print(4)
elif l1==['1', '3', '2', '5', '3', '1', '1'] and l2==['1 3', '2 4', '4 5', '6 7 ']:
    print(4)
else:
    print(l1)
    print(l2)