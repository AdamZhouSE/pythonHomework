def diffWaysToCompute(s):
    if s.isdigit():#不能用len==1判断eg.22,28
        return [int(s)]#这个需要是列表呢

    res=[]
    for i,char in enumerate(s):
        if char in ['+','-','*']:
            left=diffWaysToCompute(s[:i])
            right=diffWaysToCompute(s[i+1:])
            for l in left:
                for r in right:
                    if char == '+':
                        res.append(l + r)
                    elif char == '-':
                        res.append(l - r)
                    else:
                        res.append(l * r)
    return res

if __name__=="__main__":
    s=input()
    ans=diffWaysToCompute(s)
    print(ans)