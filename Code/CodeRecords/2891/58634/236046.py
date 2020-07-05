n = int(input())
welfares = [int(i) for i in input().split(" ")]
maxNum = max(welfares)
extra = 0
for i in range(0,n):
    extra += maxNum-welfares[i]
print(extra)