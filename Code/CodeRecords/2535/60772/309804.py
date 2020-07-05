def execute(arr):
    count = 0
    Max = 0
    for i, x in enumerate(arr):
        Max = max(Max, x)
        if Max == i:
            count += 1
    return count


s = input()
arr = []
for ele in s:
    if ele.isdigit():
        arr.append(int(ele))

print(execute(arr))
