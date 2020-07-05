n = int(input())
hi = [int]
previous = 0
result = True
for i in range(n):
    temp = [int(i) for i in input().split(" ")]
    wi = temp[0]
    hi = temp[1]
    if(previous==0):
        previous = max(wi,hi)
        continue
    if(previous < min(wi,hi)):
        result = False
        break
    if(previous >= max(wi,hi)):
        previous = max(wi,hi)
    else:
        previous = min(wi,hi)
if(result):
    print("YES")
else:
    print("NO")

