n=eval(input())
realMax=-1000
process=[[],[]]
arr=[[],[]]
winner=''
for _ in range(n):
    temp=list(input().strip().split(' '))
    temp[1]=int(temp[1])
    process[0].append(temp[0])
    process[1].append(temp[1])
    if temp[0] not in arr[0]:
        arr[0].append(temp[0])
        arr[1].append(temp[1])
    else:
        num=arr[0].index(temp[0])
        arr[1][num]+=temp[1]
for i in range(len(arr[0])):
    realMax=max(arr[1][i],realMax)
final=[arr[0],[0 for _ in range(len(arr[0]))]]
for i in range(n):
    num=arr[0].index(process[0][i])
    final[1][num]+=process[1][i]
    if(arr[1][num]==realMax)&(final[1][num]>=realMax):
        winner=final[0][num]
        break
print(winner)