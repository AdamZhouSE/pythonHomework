def diffWaysToCompute(input):
    if input.isdigit():
        return [int(input)]
    memo={}
    res=[]
    if input in memo:
        return memo[input]
    for i in range(len(input)):
        op=input[i]
        if op not in "+-*":
            continue
        left=diffWaysToCompute(input[:i])
        right=diffWaysToCompute(input[i+1:])
        for num1 in left:
            for num2 in right:
                res.append(calc(num1,num2,op))
    memo[input]=res
    return res

def calc(num1,num2,op):
    if op=="+":
        return num1+num2
    elif op=="-":
        return num1-num2
    else:
        return num1*num2

str = input()
print(diffWaysToCompute(str))
