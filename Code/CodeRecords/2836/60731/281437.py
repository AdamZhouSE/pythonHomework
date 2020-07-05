length=int(input())
data=list(map(int,input().split()))
sortdata=sorted(data)
flag=False
for i in range(length):
    data=data[length-1:]+data[:length-1]
    if data==sortdata:
        flag=True
        print(i+1)
        break
if not flag:
    print(-1)