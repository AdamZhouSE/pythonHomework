def diffWaysToCompute(input):
    mem = dict()
    return _diffWaysToCompute(input, mem)
        
def _diffWaysToCompute(input, mem):
    if input.isdigit():
        return [int(input)]
        
    if input in mem:
        return mem[input]
        
    res = list()
    for i in range(1, len(input)):
        if input[i] in "+-*":
            left = _diffWaysToCompute(input[0:i], mem)
            right = _diffWaysToCompute(input[i+1:], mem)
            for l in left:
                for r in right:                      
                    res.append(_calc(l, input[i], r))
                    
    mem[input] = res
    return res
        
def _calc(a, op, b):
    return {
        '+': a + b,
        '-': a - b,
        '*': a * b
    }[op]
print(diffWaysToCompute(input()))