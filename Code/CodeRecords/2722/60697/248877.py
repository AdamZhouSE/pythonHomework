t=int(input())
a=[]
for i in range(t):
    a.append(int(input()))
for i in a:
    if(i%5==0):
        print("YES")
    else:
        print("NO")