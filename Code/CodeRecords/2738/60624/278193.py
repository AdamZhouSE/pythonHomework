def func14():
    def helper(height:list):
        height.append(0)
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[i] < height[stack[-1]]:
                s = stack.pop()
                res = max(res,height[s]*((i-stack[-1]-1)if stack else i))
            stack.append(i)
        return res
    in_str = input()

    matrix = []
    while in_str != "]":
        in_str = input()
        temp = []
        for i in in_str:
            if i == "1":
                temp.append(1)
            elif i == "0":
                temp.append(0)
        if len(temp) != 0:
            matrix.append(temp)

    if len(matrix) == 0:
        print(0)
    else:
        ans = 0
        m, n = len(matrix), len(matrix[0])
        height = [0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    height[j] = 0
                else:
                    height[j] += 1
            ans = max(ans,helper(height))
        print(ans)
    return
func14()