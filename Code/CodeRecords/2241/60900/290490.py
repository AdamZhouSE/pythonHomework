n = int(input())
result =0
for i in range(0,n+1):
    count=0
    while(count<n):
        i+=1
        count+=i
    if count == n: result+=1

print(result)