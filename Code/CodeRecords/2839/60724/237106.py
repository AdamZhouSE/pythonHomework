s=int(input())
a=[]
for i in range(s):
    t=input()
    if t in a:
        print("YES")
    else:
        print("NO")
        a.append(t)