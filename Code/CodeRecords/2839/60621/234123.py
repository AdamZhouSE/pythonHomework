a=int(input())
b=[]
for i in range(a):
    c=input()
    if c in b:
        print("YES")
    else:
        b.append(c)
        print("NO")