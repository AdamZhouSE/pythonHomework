def findT(saleWhat,road,MAX,a,b):
   m

N=int(input())
nmk=list(map(int,input().split(' ')))
saleWhat=list(map(int,input().split('')))
road=[]
for i in range(nmk[1]):
    road.append(list(map(int,input().split(''))))
ab=list(map(int,input().split('')))
k=nmk[2]
a=ab[0]
b=ab[1]
findT(saleWhat,road,k,a,b)