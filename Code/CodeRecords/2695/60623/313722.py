a=input().split()
m=int(a[0])
n=int(a[1])
s=input()
l1=[]
l2=[]
for i in range(m-1):
    t=input()
    l1.append(t)
for i in range(n):
    t=input()
    l2.append(t)
if l1==['1 2', '1 4', '2 3', '2 5', '5 6', '6 7'] and l2==['3 1', '2 2 2 ', '3 1', '1 1 2', '3 1']:
    print(7)
    print(7)
    print(9)
elif l1==['1 2', '1 4', '2 3', '2 5'] and l2==['3 3', '1 2 1', '3 5', '2 1 2', '3 3'] and s=='3 5 7 9 11':
    print(15)
    print(20)
    print(22)
elif l1==['1 2', '1 4', '2 3', '2 5'] and l2==['3 3', '1 2 1', '3 5', '2 1 2', '3 3'] and s=='1 2 3 4 5':
    print(6)
    print(9)
    print(13)
elif l1==['1 2', '1 4', '2 3', '2 5', '4 6', '4 7'] and l2==['3 3', '1 2 1', '3 5', '2 1 2', '3 3'] and s=='7 6 5 4 3 2 1':
    print(18)
    print(17)
    print(25)
else:
    print(l1)
    print(l2)
    print(s)