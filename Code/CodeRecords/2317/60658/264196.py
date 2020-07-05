li = [int(x) for x in input().split(",")]
li.sort()
ans = 0
for i in range(len(li)):
    for j in range(i+1,len(li)):
        ans+= 2**(j-i-1)*(li[j]-li[i])
print(ans)