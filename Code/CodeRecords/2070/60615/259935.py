
base=float(input())
exp=int(input())
result=1
if exp>=0:
    for i in range(0, exp):  # exp>=0
        result = result * base
    print(result)
else:
    for i in range(exp, 0):  # exp>=0
        result = result / base
    print(result)


