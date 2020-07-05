n=int(input())
years=list(map(int,input().split(' ')))
levels=list(map(int,input().split(' ')))
years.append(0)
cur=levels[0]
twd=levels[1]
time=0
for i in range(cur-1,twd-1):
    time+=years[i]
print(time)