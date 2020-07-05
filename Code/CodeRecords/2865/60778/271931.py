n=int(input())
m=int(input())
ar=[]
for i in range(n):
    ar.append(int(input()))
ar.sort(reverse=True)
sum_a=0
count=0
for aI in ar:
    sum_a+=aI
    count+=1
    if(sum_a>=m):
        break;
print(count)
