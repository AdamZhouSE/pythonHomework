n,q= map(int, input().split())
frequent = [0]*(n+1)
result = 0
array = [int(i) for i in input().split(" ")]
for i in range(q):
    l,r = map(int, input().split())
    for j in range(l,r+1):
        frequent[j] +=1
array.sort()
array.reverse()
frequent.sort()
frequent.reverse()
for i in range(n):
    result+=array[i]*frequent[i]
print(result)
