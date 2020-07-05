nums=int(input())
packet=list(map(int,input().split()))
target=sum(packet)%2
count=0
for p in packet:
    if(p%2==target):
        count+=1
print(count)