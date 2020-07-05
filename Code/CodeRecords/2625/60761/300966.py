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
                if preOutStr:
                    helper(i + 1, preOutStr + '+' + cur, preSum + curValue, curValue)
                    helper(i + 1, preOutStr + '-' + cur, preSum - curValue, -curValue)
                    helper(i + 1, preOutStr + '*' + cur, preSum - preValue + curValue * preValue, curValue * preValue)
                else:
                    helper(i + 1, cur, curValue, curValue)
        helper(0, '', 0, 0)
        return res

num=input()
target=int(input())
print(addOperators(num,target))
