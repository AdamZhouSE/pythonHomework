op=str(input())
res=[]
def solve(op):
    res=[]
    for i in range(len(op)):
        if op[i] in ['+', '-', '*']:
            # 遇到运算符，计算左右两侧的结果集
            # 递归函数求出子问题的解
            left = solve(op[:i])
            right = solve(op[i+1:])
            #根据运算符合并子问题的解
            for l in left:
                for r in right:
                    if op[i] == '+':
                        res.append(l + r)
                    elif op[i] == '-':
                        res.append(l - r)
                    else:
                        res.append(l * r)
    if len(res)==0:
        return [int(op)]
    return res

res=solve(op)
print(res)