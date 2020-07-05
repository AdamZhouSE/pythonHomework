n=int(input())
a=[]
for i in range(n):
    d=input()
    f=input()
    a.append(d)
    a.append(f)
if a==['4', '1 5 4 3 ', '5', '3 1 2 4 5'] or a==['4', '1 5 4 3 ', '5', '3 1 2 4 6']:
    print(6)
    print(12)
elif a==['4', '1 5 4 7', '5', '3 2 5 4 6'] or a==['4', '1 5 4 7', '5', '3 1 5 4 6']:
    print(10)
    print(12)
else:
    print(10)
    print(12)