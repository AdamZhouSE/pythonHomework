def addOperators(num, target):
    res = []
    def helper(index, preOutStr, preSum, preValue):
        if index == len(num):
            if preSum == target:
                res.append(preOutStr)
            return
        if max(1, abs(preValue)) * (int(num[index:])) < abs(target - preSum):
            return
        for i in range(index, index + 1 if num[index] == '0' else len(num)):
            cur = num[index:i + 1]
            curValue = int(cur)
            if not preOutStr:
                helper(i + 1, cur, curValue, curValue)
            else:
                helper(i + 1, preOutStr + '+' + cur, preSum + curValue, curValue)
                helper(i + 1, preOutStr + '-' + cur, preSum - curValue, -curValue)
                helper(i + 1, preOutStr + '*' + cur, preSum - preValue + curValue * preValue, curValue * preValue)
    helper(0, '', 0, 0)
    return res

a=input()
b=int(input())
print(addOperators(a,b))