def cal(num):
    res = 0
    for x in range(1,num + 1):
        res += pow(x,2)
    return res

n = eval(input())
while(n != 0):
    n = n - 1
    print(cal(eval(input())))