n=int(input())
list4=input().split()
a=[]
a.append(0)
for i in range(n):
    a.append(int(list4[i]))
flag=0
for i in range(1,n+1):
    if i==a[a[a[i]]]:
        flag=1;
        break;
if flag==1:
    print("YES")
else:
    print("NO")