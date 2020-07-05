target=int(input())
target = abs(target)
k = 0
while target > 0:
    k += 1
    target -= k
ans=0
if target % 2 == 0:
    ans= k  
else:
    ans=k + 1 + k%2
print(ans)
