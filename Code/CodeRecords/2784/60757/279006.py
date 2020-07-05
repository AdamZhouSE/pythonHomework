li=input().split()
n=int(li[0])
m=int(li[1])
city=[]
for i in range(m):
    aj=list(map(int,input().split()))
    city.append(aj.index(max(aj))+1)
maxcount=0
maxp=1
for i in range(n):
    if city.count(i+1)>maxcount:
        maxp=i+1
        maxcount=city.count(i+1)
print(maxp)