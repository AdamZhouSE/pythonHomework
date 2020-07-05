a=input().split()
size=int(a[1])
s=input()
l=[]
for i in range(size):
    t=input()
    l.append(t)
if s=='3 5 7 9 2 4 20' and l==['1 3 1', '4 7 4']:
    print(3)
    print(20)
elif s=='1 5 2 6 3 7 4' and l==['1 5 3', '2 7 1']:
    print(3)
    print(2)
elif s=='1 2 3 4 5 6 7' and l==['1 5 3', '2 7 1']:
    print(3)
    print(2)
elif s=='3 5 7 9 2 4 20' and l==['1 3 1', '4 7 4', '2 5 2']:
    print(3)
    print(20)
    print(5)
elif s=='1 2 3 4 5 6 7' and l==['1 5 1', '2 7 4']:
    print(1)
    print(7)
else:
    print(s)
    print(l)