def func5():
    left = int(input())
    right = int(input())
    res = []
    def helper(operand:int):
        length = len(str(operand))
        i, j = 0, operand
        while length>0:
            i = j%10
            j = j // 10
            if i == 0 or operand%i != 0:
                break
            length -= 1
        if length == 0:
            res.append(operand)
        return
    for i in range(left, right+1, 1):
        helper(i)
    print(res)
    return
func5()