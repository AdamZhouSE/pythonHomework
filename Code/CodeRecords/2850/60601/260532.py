def solve(num:list,k:int):
    Max = num.count(1)
    for i in range(len(num)-k+1):
        newNum = list(num)
        for j in range(0,k):
            newNum[i+j] = 1 - newNum[i+j]
        Max = max(Max,newNum.count(1))
    return Max

n = eval(input())
num = list(map(int,input().split(' ')))
Max = num.count(1)
for i in range(n,0,-1):
    Max = max(Max,solve(num,i))
print(Max)
