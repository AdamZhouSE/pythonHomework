num1=list(input().split(","))
num1[0]=num1[0][1:len(num1[0])]
num1[-1]=num1[-1][0:-1]
n=len(num1)
print(num1)
for i in range(n):
    num1[i]=int(num1[i])
num2=sorted(num1,reverse=True)
res=[]
for i, b in enumerate(num2):
    j = num1.index(b) + 1
    num1[: j] = num1[j - 1: : -1]
    num1[: n - i] = num1[n - i - 1: : -1]
    res += [j, n - i]
print(res)