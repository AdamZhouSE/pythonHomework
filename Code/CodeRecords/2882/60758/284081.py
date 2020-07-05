n=int(input())
top=list(map(int,input().split()))
leak=max(top)
k=top.index(leak)
temp=top.copy()
temp.reverse()
p=temp.index(leak)
conti=True
for i in range(0,k-1):
    if(top[i]>top[i+1]):
        print('No')
        conti=False
        break
if(conti):
    for i in range(p+1,n-1):
        if top[i]<top[i+1]:
            print('No')
            break
        if(i==n-2):
            print("Yes")