tests = int(input())
for i in range(0,tests):
    ls = input().split(' ')
    num1 = int(ls[0],2)
    num2 = int(ls[1],2)
    res = num1*num2
    print(res)