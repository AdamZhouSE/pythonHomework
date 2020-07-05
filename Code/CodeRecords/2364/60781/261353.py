
n=int(input())
count=0
i=1
while i<=n:
    if(i%11==0 or i%100==0):
        count+=1
    i+=1
print(count)