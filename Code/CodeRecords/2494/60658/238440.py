li = [int(x) for x in input()[1:-1].split(",")]
ans = 0
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[j]*2<li[i]:
            ans+=1
print(ans)