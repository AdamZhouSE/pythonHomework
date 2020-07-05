def diffWaysToCompute(s):
    end = []
    op = {'+': lambda x, y: x + y,
          '-': lambda x, y: x - y,
          '*': lambda x, y: x * y}
    for i in range(len(s)):
        if s[i] in op.keys():
            for left in diffWaysToCompute(s[:i]):
                for right in diffWaysToCompute(s[i + 1:len(s)]):
                    output = op[s[i]](left, right)
                    end.append(output)
    if len(end) == 0:
        end.append(int(s))
    return end


s = str(input())
nums = diffWaysToCompute(s)
print(nums)