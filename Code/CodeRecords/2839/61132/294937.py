n=int(input())
l=[]
for i in range(n):
    tmp=input()
    if tmp in l:
        print("YES")
    else:
        l.append(tmp)
        print("NO")