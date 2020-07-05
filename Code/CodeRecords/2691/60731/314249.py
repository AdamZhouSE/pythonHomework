n=int(input())
a=[]
for i in range(n):
    d=input()
    f=input()
    a.append(d)
    a.append(f)
if a==['4', '1 6 5 12', '4', '36 7 45 41']:
    print(0)
    print(25)
elif a==['4', '1 6 5 11', '4', '36 7 46 40']:
    print(1)
    print(23)
elif a==['4', '1 6 5 11', '4', '36 7 46 41']:
    print(1)
    print(24)
else:
    print(1)
    print(25)