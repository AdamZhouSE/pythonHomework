arr = [int(x) for x in input().split(",")]
target = int(input())
length = len(arr)
first = target//length
cur = first
offset = dict()
while True:
    sum = 0
    for i in arr:
        if i < cur:
            sum+=i
        else:
            sum+=cur

    if(sum>=target):
        offset[cur] = abs(sum-target)
        break
    else:
        offset[cur] = abs(sum-target)
        cur+=1

reslist = sorted(offset.items() , key=lambda item:item[1])
print(reslist[0][0])