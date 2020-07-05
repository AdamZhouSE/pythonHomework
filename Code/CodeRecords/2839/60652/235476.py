n=int(input())
l=[]
for i in range(0,n):
    name=input()
    if name in l:
        print("YES")
    else:
        l.append(name)
        print("NO")