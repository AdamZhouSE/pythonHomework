num = int(input())


def cal(a):
    string = str(a)
    result = 0
    for i in range(len(string)):
        result += int(string[i]) * int(string[i])
    return result


fast = num
isOne = True
while num != 1:
    num = cal(num)
    fast = cal(fast)
    fast = cal(fast)
    if fast == 1:
        break
    if num == fast:
        isOne = False
        break
print(isOne)
