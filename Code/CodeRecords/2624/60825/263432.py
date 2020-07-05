memo = {}

def diffWaysToCompute(input):
    formula = input
    return _diffWaysToCompute(0, len(input))

def _diffWaysToCompute(lo, hi):
    if formula[lo:hi].isdigit():
        return [int(formula[lo:hi])]
    if((lo, hi) in memo):
        return memo.get((lo, hi))
    ret = []
    for i, char in enumerate(formula[lo:hi]):
        if char in ['+', '-', '*']:
            leftResult = _diffWaysToCompute(lo, i + lo)
            rightResult = _diffWaysToCompute(lo + i + 1, hi)
            ret.extend([eval(str(i) + char + str(j)) for i in leftResult for j in rightResult])
            memo[(lo, hi)] = ret
    return ret

a=input()
print(diffWaysToCompute(a))