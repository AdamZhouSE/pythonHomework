import ast


def solve(data,lower,higher):
    sum = []
    temp = 0
    res = 0
    for i in range(0,len(data)):
        temp = temp + data[i]
        sum.append(temp)
    for i in range(0,len(sum)):
        h_index = len(sum) - 1
        l_index = i
        if lower <= sum[i] <= higher:
            res = res + 1
        for j in range(len(sum) - 1,-1,-1):
            if sum[j] <= sum[i] + higher:
                h_index = j
                break
        for j in range(i+ 1,h_index):
            if sum[j] >= sum[i] + lower:
                l_index = j
                break
        res = res + h_index - l_index
    return res


data = ast.literal_eval(input())
low = int(input())
high = int(input())
print(solve(data,low,high))