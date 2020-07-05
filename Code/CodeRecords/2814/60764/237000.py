a=int(input())
n=list(map(int,input().split()))
satisfied=0
time=0
for i in range(a):
    tem=n.pop(n.index(min(n)))
    if tem>=time:
        time+=tem
        satisfied+=1
print(satisfied)