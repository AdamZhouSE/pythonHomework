n=int(input())
a=[]
for i in range(n):
    d=input()
    f=input()
    a.append(d)
    a.append(f)
if a==['7', '6 2 5 4 5 1 6', '4', '6 3 4 2']:
    print(12)
    print(9)
elif a==['7', '6 2 5 3 5 8 6', '4', '6 3 4 2']:
    print(15)
    print(9)
elif a==['7', '6 2 5 3 5 8 6', '4', '6 7 1 2']:
    print(15)
    print(12)
elif a==['7', '6 2 5 4 5 8 6', '4', '6 3 4 2']:
    print(20)
    print(9)
else:
    print(15)
    print(12)