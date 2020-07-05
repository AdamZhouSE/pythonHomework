temp=input().split()
p,n=temp[0],temp[1]
store=[]
for i in range(n):
    num=input()%p
    if(num in store):
        print(i)
    else:
        store.append()
else:
    print(-1)