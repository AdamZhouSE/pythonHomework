temp=input().split()
p,n=int(temp[0]),int(temp[1])
store=[]
for i in range(n):
    num=int(input())%p
    if(num in store):
        print(i+1)
        break
    else:
        store.append(num)
else:
    print(-1)
