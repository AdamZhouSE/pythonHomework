n = int(input())
li = [int(x) for x in input().split()]
ans=0
for i in range(1,len(li)):
    for j in range(i,len(li)):
        a = sum(li[:i])
        b = sum(li[i:j])
        c = sum(li[j:])
        if a==b and b==c:
            ans+=1
print(ans)