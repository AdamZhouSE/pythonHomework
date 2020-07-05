from fractions import Fraction
def calculate(a):   
    result = 0
    plussub = []
    nums = []
    for i in range(len(a) - 1, -1, -1):
        if a[i] == '+' or a[i] == '-':
            if a[i] == '+':
                plussub.append(1)
            else:
                plussub.append(-1)
            a.remove(a[i])
    plussub = plussub[::-1]    
    for i in range(0, len(a), 3):
        nums.append(Fraction(int(a[i]), int(a[i + 2])))   
    for i in range(len(nums)):
        result = result + plussub[i] * nums[i]
    if float(result) % 1 == 0:
        result = str(result) + str('/1')
    print(result)
a = list(input())
if a[0] != '-':
    a = ['+'] + a
calculate(a)