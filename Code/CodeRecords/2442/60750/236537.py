import ast
def solve(data):
    data.sort()
    maxNum = 0
    if len(data) < 2:
        return 0
    for i in range(0,len(data) - 1):
        maxNum = max(maxNum, int(abs(data[i + 1] - data[i])))
    return maxNum
str_list = input()
list_new = ast.literal_eval(str_list)
print(solve(list_new))
