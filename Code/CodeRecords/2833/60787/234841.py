n=int(input())
v=0
list=[]
for i in range(0,n):
    a,b=map(int,input().split())
    v+=a
    list.append(b)
list=sorted(list)
if v>list[n-2]+list[n-1]:
    print("NO")
else:
    print("YES")