n=int(input())
count=0
for i in range(0,10**n+1):
    if(i<100 and i%11==0)or(i>100 and i%111==0):
        count+=1
print(10**n-count)