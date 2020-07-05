exp=input().split("+")
exp.sort()
for i in range(len(exp)-1):
    print(exp[i]+"+",end="")
print(exp[-1])