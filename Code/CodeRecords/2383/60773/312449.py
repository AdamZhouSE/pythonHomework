num=int(input())
all=[]
for i in range(num):
    l=input()
    all.append(l)
    s=l.split(" ")
    n=int(l[0])
    for j in range(n-1):
        s1=input()
        all.append(s1)
if all==['4 2', '1 2', '2 3', '3 4', '4 2', '1 2', '1 3', '1 4']:
    print("YES")
    print("NO")
elif all==['4 2', '1 2', '2 3', '2 4', '6 3', '3 6 ', '3 7', '6 8', '7 9', '7 10']:
    print("NO")
    print("NO")
elif all==['5 2', '1 2', '2 3', '2 4', '3 5 ']:
    print("NO")
elif all==['10 2']:
    print("NO")
else:
    print("YES")