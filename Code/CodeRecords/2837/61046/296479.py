test=input().split()
n=int(test[0])
l=int(test[1])
r=int(test[2])
min=[]
max=[]
count=[]
k=0
for i in range(1,n):
    count.append(pow(2,i))
for i in range(l-1):
    min.append(count[i])
while len(min)<n:
    min.append(1)
for i in range(r-1):
    max.append(count[i])
    k+=1
while len(max) < n-1:
    max.append(count[k-1])
max.append(1)

print(sum(min),sum(max))