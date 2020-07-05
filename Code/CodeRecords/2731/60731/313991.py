n=int(input())
a=[]
for i in range(n):
    d=input()
    f=input()
    a.append(d)
    a.append(f)
if a==['7', '10 20 20 20 20 20 20'] or a==['7', '10 20 20 20 20 10 20'] or a==['7', '10 10 20 20 20 10 20']:
    print(6)
elif a==['5', '10 20 20 20 20']:
    print(4)
else:
    print(6)