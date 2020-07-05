n = int(input())
li = [int(x) for x in input().split()]
s =set()
ans = 0
for i in li:
    while i in s:
        i+=1
        ans+=1
    s.add(i)
print(ans)