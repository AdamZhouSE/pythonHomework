n=int(input())
years=input().split(" ")
ranks=input().split(" ")
now=int(ranks[0])-1
future=int(ranks[1])-1
res=0

for i in range(now,future):
    res+=int(years[i])

print(res)