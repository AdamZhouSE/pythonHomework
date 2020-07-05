n=int(input())
m=int(input())
a=[]
numOfU=0
for i in range(n):
    ai=int(input())
    a.append(ai)
a.sort(reverse=True)
while m>0:
    k=a[numOfU]
    m-=k
    numOfU+=1
print(numOfU)