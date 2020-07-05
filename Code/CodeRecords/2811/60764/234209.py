a=input().split()
c=0
for i in range(len(a)):
    a[i]=int(a[i])
List=[0 for k in range(a[0])]
for j in range(a[1]):
    tem=int(input())
    n=tem%a[0]
    if List[n-1]==0:
        List[n-1]=-1
    else:
        print(j+1)
        c=1
        break
if c==0:
    print(-1)