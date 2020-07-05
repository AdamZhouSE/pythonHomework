n=int(input())
years=input().split()
a,b=map(int,input().split())
for i in range(len(years)):
    years[i]=int(years[i])
print(sum(years[a-1:b-1]))