n=int(input())
year=input().split(" ")
year=list(int(a) for a in year)
gra=input().split(" ")
gra=list(int(a) for a in gra)
a=gra[0]
b=gra[1]
sumy=0
for x in range(a-1,b-1):
    sumy=sumy+year[x]
print(sumy)