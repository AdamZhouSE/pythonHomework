num = int(input())
for j in range(num):
    arr = list(input())
    res = ""
    stack = []
    count = 1
    for i in arr:
        if i == "(":
            res += str(count) + " "
            stack.append(count)
            count += 1
        elif i == ")":
            res += str(stack.pop(-1)) + " "
    print(res)