n=int(input())
count=0
for i in range(2,n+1):
    for j in range(2,int(n**0.5)+1):
        if i%j==0:
            count+=1
print(count%(10**9)+7)