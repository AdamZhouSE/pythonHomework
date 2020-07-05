def find(arr,target):
    arr.sort(reverse=True)
    arr.append(0)
    sums, pos = sum(arr), 0
    while sums > target:
        sums -= (arr[pos] - arr[pos + 1]) * (pos + 1)
        pos += 1
    if pos:
        div, mod = divmod(target - sums, pos)
        return arr[pos] + div + 1 * (mod > pos / 2)
    else:
        return arr[pos]

arr = list(map(int, input().replace("[", "").replace("]", "").split(",")))
target =int(input())
res=find(arr,target)
print(res)