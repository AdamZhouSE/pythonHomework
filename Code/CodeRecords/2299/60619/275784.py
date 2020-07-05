def make_mid_tree(numbers):
    if len(numbers) == 0:
        return "#"
    elif len(numbers) == 1:
        return str(numbers[0])
    else:
        left = []
        right = []
        mid = int(numbers[0])
        for i in range(1, len(numbers)):
            if numbers[i] > mid:
                right.append(numbers[i])
            else:
                left.append(numbers[i])
        return str(mid)+make_mid_tree(left) + make_mid_tree(right)


n = int(input())
while n != 0:
    oriStr = input()
    oriNum = [int(c) for c in oriStr]
    standard = make_mid_tree(oriNum)
    for ind in range(n):
        target = input()
        inputNum = [int(c) for c in target]
        judge = make_mid_tree(inputNum)
        if judge == standard:
            print("YES")
        else:
            print("NO")
    n = int(input())
