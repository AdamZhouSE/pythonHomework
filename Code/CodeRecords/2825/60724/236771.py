sNo=int(input())
score=0
z=[]
rank=1
temp=0
for i in range(sNo):
    if i==0:
        z=input().split()
        score=int(z[0])+int(z[1])+int(z[2])+int(z[3])
    else:
        z=input().split()
        temp=int(z[0])+int(z[1])+int(z[2])+int(z[3])
    if temp>score:
        rank=rank+1
print(rank)