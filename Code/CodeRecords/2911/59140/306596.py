temp = [int(x) for x in input().split(" ")]
n, m = temp[0], temp[1]
arr = [int(x) for x in input().split(" ")]
if m == 0:
    print(sum(arr))
else:
    ans = [[int(x) - 1 for x in input().split(" ")]]
    index = 0
    for _ in range(1, m):
        temp = [int(x) for x in input().split(" ")]
        if ans[index].count(temp[0] - 1) == 0 and ans[index].count(temp[1] - 1) == 0:
            ans.append(temp)
            index += 1
        elif ans[index].count(temp[0] - 1) == 1 and ans[index].count(temp[1] - 1) == 0:
            ans[index].append(temp[1] - 1)
        elif ans[index].count(temp[0] - 1) == 0 and ans[index].count(temp[1] - 1) == 1:
            ans[index].append(temp[0] - 1)
        else:
            ans[index].append(temp[0] - 1)
            ans[index].append(temp[1] - 1)
    result = sum(arr)
    for i in ans:
        temp=[arr[x] for x in i]
        result = result - sum(temp) + min(temp)
    print(result)