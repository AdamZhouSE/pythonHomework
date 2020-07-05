t=int(input())
n=int(input())
l=input()
i=0
sum=0
count=0
for i in range(n+1):
    for j in range(i+1,n+1):
        count=0
        if l[i-1]<l[j-1]:
            count+=0
            j+=1
        if l[i-1]>l[j-1]:
            count+=1
            j+=1
    sum+=count 
print(sum)
    
    
    