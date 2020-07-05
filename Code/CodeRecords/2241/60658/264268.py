target = int(input())
ans = 0
i = 1
while target>0:
    ans+=(target%i==0)
    target-=i
    i+=1
print(ans)