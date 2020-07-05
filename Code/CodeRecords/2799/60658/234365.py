n = int(input())
li = [int(x) for x in set(input().split())]
ans=set()
for i in li:
    while i%2==0:
        i=int(i/2)
    while i%3==0:
        i=int(i/3)
    ans.add(i)
print("Yes" if len(ans)==1 else "No")
    