a=int(input())
b=input().split()
c=input().split()
year=0
for d in range(a-1):
    b[d]=int(b[d])
for e in range(2):
     c[e]=int(c[e])
level=c[0]-1
while level<c[1]-1:
    year+=b[level]
    level+=1
print(year)