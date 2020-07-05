sources=eval(input())
lower=int(input())
upper=int(input())
sums=[]
for i in range(len(sources)):
    for j in range(i,len(sources)):
        sum_0=0
        for a in range(i,j+1):
            sum_0+=sources[a]
        sums.append(sum_0)
count=0
for i in sums:
    if i>=lower and i<=upper:
        count+=1
print(count)