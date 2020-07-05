length=int(input())
data=list(map(int,input().split()))
sortdata=sorted(data)
flag=False
if data==sortdata:
    print(0)
    flag=True
else:
    for i in range(length):
        data=data[length-1:]+data[:length-1]
        if data==sortdata:
            flag=True
            print(i+1)
            break
if not flag:
    print(-1)