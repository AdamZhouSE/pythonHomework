n=int(input())
name=[-1]*n
for i in range(0,n):
    na=input()
    if(na in name):
        print("YES")
    else:
        print("NO")
    name[i]=na
     